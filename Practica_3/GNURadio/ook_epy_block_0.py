import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following:
	This block implements a voltage-controlled oscillator (VCO) in the digital domain.
Its main function is to generate a sinusoidal signal whose amplitude and phase can be controlled externally using the block's inputs.
The block receives two float inputs (32-bit floating-point numbers)
and produces a float output.
First input: Amplitude: This input controls the amplitude of the sinusoidal signal. Each sample received at this input directly multiplies
the amplitude of the generated wave. If a constant is entered, the signal will have a fixed amplitude; if it varies over time,
the output will reflect that amplitude modulation.
Second input: Phase: Corresponds to the instantaneous phase added to the carrier angle.
It allows the signal to be shifted in time (phase shift) or even phase modulated if this input changes over time.
Output: Modulated sinusoidal signal"""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])



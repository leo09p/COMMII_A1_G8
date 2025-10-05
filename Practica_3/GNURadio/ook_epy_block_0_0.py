import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following:
	      This block implements a baseband voltage-controlled oscillator (CE VCO or Complex Exponential VCO).
        Its function is to generate a complex baseband signal whose amplitude and phase are controlled by the block's inputs.
        Unlike the RF VCO (which generates a real passband signal with center frequency fc), this block operates in the complex domain
        and does not use an explicit carrier frequency parameter.
        First input: Amplitude: This is a vector of values ​​that control the magnitude of the complex output signal.
        If a constant value (for example, 1.0) is entered, the output will have a fixed amplitude. If the amplitude varies over time,
        amplitude modulation (AM) is generated.
        Second input: Phase: This directly represents the instantaneous phase of the complex signal. Each sample in this input defines the angle of the complex exponential.
        By varying this input over time, phase modulation (PM) or frequency modulation (FM) can be implemented, depending on how the phase evolves.
        Output: Complex baseband signal."""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])

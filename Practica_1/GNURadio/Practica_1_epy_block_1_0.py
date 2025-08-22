import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Diff',  # Nombre en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.ultimo_muestra = 0.0  # Guardamos la última muestra del bloque anterior

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]
        N = len(x)

        # Calculamos la diferencia entre muestras consecutivas
        # Para la primera muestra, usamos la última del bloque anterior
        y[0] = x[0] - self.ultimo_muestra

        # Para el resto, diferencia directa dentro del bloque
        if N > 1:
            y[1:] = x[1:] - x[:-1]

        # Guardamos la última muestra para el próximo bloque
        self.ultimo_muestra = x[-1]

        return len(y)

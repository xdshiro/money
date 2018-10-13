#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import scipy
import pylab
import numpy as np
from scipy.fftpack import fft,ifft
fileNAME='USD'
fl_open=open(fileNAME,'r')
ZZZ=np.loadtxt(fl_open,dtype=complex)
fl_open.close()
ZZZ=np.abs(ZZZ)
dMAS=ZZZ[:,1]
tMAS=ZZZ[:,0]
N=np.shape(tMAS)[0]
tMAS=tMAS-(tMAS[N-1]+tMAS[0])/2
w1, w2 = -1.* 2 *scipy.pi * N / (2 * (tMAS[N-1] - tMAS[0])), 1.* 2 *scipy.pi * N / (2 * (tMAS[N-1] - tMAS[0]))
wMAS = np.linspace(w1, w2, np.shape(ZZZ)[0])
pylab.plot(tMAS, dMAS, 'b',lw=7)
pylab.show()
dsMAS=fft(dMAS)
pylab.plot(fft(dMAS), 'r', lw=7)
pylab.show()
dMAS=ifft(dsMAS*scipy.e**(1j*wMAS*30))
pylab.plot(np.abs(tMAS), dMAS, 'b',lw=7)
pylab.show()

pylab.show()
pylab.close()
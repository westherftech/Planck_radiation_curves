# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:48:25 2022

@author: wnewton
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#%%
#Global constant and variable definitions
#-----------------------------------------------------------------------------#
f_start=100000 #Start frequency # For use with downconverted signal
f_stop=1e16 #Stop frequency  # For use with downconverted signal
numPoints=10000000 #Number of measurement points
k=1.38e-23 #Boltzman's constant
h=6.62607015e-34 #plancks constant
c=2.99792458e8 # speed of light in a vacuum
ec=math.e #eulers constant

freq_arr=np.linspace(f_start,f_stop,numPoints,endpoint= True)

def spectral_energy_density(freq,temp):
    """A function that calculates the planck spectral energy density for a given freqeuncy and temperature"""
    
    B=(2*h*freq**3)/(c**2)*(1/(ec**((h*freq)/(k*temp))-1))
    return B

plt.figure(1)
plt.clf()
plt.plot(freq_arr,spectral_energy_density(freq_arr,6000),label="T=6000 K Sun")

plt.plot(freq_arr,spectral_energy_density(freq_arr,300),label="T=300 K Room Temperature")
plt.plot(freq_arr,spectral_energy_density(freq_arr,3),label="T=3 K CMB")

plt.title("Planck-radiation-law curves for black-body radiator at 3 different temperatures")
plt.xlabel("Frequency (Hz) ")
plt.ylabel(r"$B(v)W m^{-2}Hz^{-1}rad^{-2}$")

#plt.plot([18.36e9, 18.36e9], [1e-24, 1],label="18.36 GHz")
#plt.plot([25.5e6, 25.5e6], [1e-24, 1], label="25.5 MHz")


#plt.plot([7.687e14, 7.687e14], [1e-24, 1],label="769 THz")
#plt.plot([3.997e14, 3.777e14], [1e-24, 1], label="400 THz")
plt.axvspan(13e6,275e9 , alpha=0.2, lw=0)
plt.axvspan(3.997e14,7.687e14 , color='green',alpha=0.2, lw=0)

plt.legend(loc='upper left')
plt.yscale('log')
plt.xscale('log')
plt.ylim((1e-24,1))
#plt.xlim((6.4,7.2))
fig = plt.gcf()
fig.set_size_inches(9, 5)
plt.savefig('spectral-radiance.svg', bbox_inches='tight')
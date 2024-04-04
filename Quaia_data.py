import numpy as np
import astropy as astro
import matplotlib.pyplot as plt
from astropy.io import fits

#reading in Quaia data
pathname = "/Users/Greta/Downloads/quaia_G20.0.fits"
hdu_lists_guaia = fits.open(pathname)

#choosing the main HDU
quaia_data = hdu_lists_guaia[1].data

#acessing the rp and bp spectra
rp = quaia_data["phot_rp_mean_mag"]
bp = quaia_data["phot_bp_mean_mag"]

#plotting spectra
plt.scatter(bp, rp, s=5, alpha=0.25)
plt.xlabel('BP Mean Magnitude')
plt.ylabel('RP Mean Magnitude')
plt.title('Color-Color Diagram')
plt.grid(True)
plt.show()
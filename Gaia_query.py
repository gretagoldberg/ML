import numpy as np
import astropy as astro
import matplotlib.pyplot as plt
from astropy.io import fits


import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

#performing cone search centered at specific RA/Dec coordinates
Gaia.ROW_LIMIT = 10 #limiting to only ten rows
cordinates = SkyCoord(ra=280, dec=-60, unit=(u.degree, u.degree), frame='icrs') #degrees in the ICRS coordinate frame
job = Gaia.cone_search_async(cordinates, radius=u.Quantity(5.0, u.deg),) #job to submit asynchronously

#checking the status of the query
while not job.is_finished():
    print("Satus: ", job.status)

try:
    results = job.get_results
    results.pprint()
except:
    print("we tried :( )")

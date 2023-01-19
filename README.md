# University-MISC

Hello, if you are here to:

 - see the Moon Illumination code - please find the moon illumination.py file above.
 - see the Special remarks table - please find the ascii table within the sepcial remarks table.txt file above.
 - see the JO1 sample ETC input table - please find the ascii table within the JO1 table.txt file above.

Justifications for the ETC inputs found within the JO1 table:
- angular diameter - Semi majour axis estimate taken from SIMBAD query using target coordinates (10h41m43.872s	-08d25m11.352s)
- Spectral distribution - S0 morphological estimates taken from visual inspection of the DSS cutout displayed on SIMBAD query for target coordinates and morphological classification of wings data by Fasano et al. in 2006.
- B band magnitude - data taken from SIMBAD query using target coordinates
- Redshift - data taken from the OMEGAWINGS children catalogue from Poggianti et al. 2015
- Instrument mode - NFM per our scientific objective of increased spatial resolution
- Moon FLI - code written using ephem python library available at shorturl.at/yNX89
- airmass  - calculated from $\frac{1}{cos(ZA)}$ where ZA represents the zenith angle
- seeing - conditions assumed from very similar run conditions performed by Knapen et al. 2018 where the best measurements were obtained with seeing below 0.6"
- NDIT - number of observations calculated from the minimum number of mosaic tiles required to cover the entire galaxy
- DIT - exposure time taken from similar conditions in Knapen et al. 2018 and fine tuned to reach the required SNR and lunar conditions

Thanks,

Group 1d

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:19:04 2023

@author: George Hine
 email:  PPYGH3@nottingham.ac.uk
 
"""
import ephem 

def moon_illumination(Lat,Long,Date_time):
    '''
    

    Parameters
    ----------
    Lat : Latitude of telescope
    
    Long : Longitude of telescope
    
    Date_time : Date-Time in format 'YYYY-MM-DD HH:MM:SS'

    Returns
    -------
    illumination : percentage illumination of the moon

    '''
    
    # Define observer latitude and longitude
    observer = ephem.Observer()
    observer.lat = Lat # latitude in decimal degrees
    observer.lon = Long # longitude in decimal degrees
    
    # Define date and time
    date_time = Date_time # format: YYYY/MM/DD HH:MM:SS
    observer.date = date_time
    
    # Create a Moon object
    moon = ephem.Moon()
    
    # Calculate the moon's phase
    moon.compute(observer)
    
    # Get the illumination as a percentage
    illumination = moon.moon_phase * 100
    
    print('Moon illumination on {}: {:.2f}%'.format(date_time, illumination))
    return illumination 
from finch import Finch
import KonamiKoders

from time import sleep

finch = Finch()

bodies = 0 # The initial counter
bodies_max = 1 # The maximum number of bodies 
mode = 'search' # Set the mode for the finch as search

ambient_temp = '%5.2f' % finch.temperature()

finch666 = KonamiKoders.OurFinch() # finch666 is equal to the class name

#finch666.init()

#finch666.goninja(bodies, bodies_max, mode) # From the class run goninja

#finch666.findthelight()

while True:
    print (ambient_temp())
    print ('Temperature %5.2f' % finch.temperature())

# iPhone is basicaly the same temp as air
# My hand is 23.33 when room temp == 22.08
# Aprox. bottle 25.42

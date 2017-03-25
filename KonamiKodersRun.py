import KonamiKoders
finch = Finch()
from finch import Finch

from time import sleep

bodies = 0 # The initial counter
bodies_max = 3 # The maximum number of bodies 
mode = 'search' # Set the mode for the finch as search

finch666 = KonamiKoders.OurFinch() # finch666 is equal to the class name

#finch666.init()

#finch666.goninja(bodies, bodies_max, mode) # From the class run goninja

#finch666.findthelight()


# iPhone is basicaly the same temp as air
# My hand is 23.33 when room temp == 22.08
# Aprox. bottle 25.42


left_light, right_light = finch.light()
print ('Lights %5.3f, %5.3f' % (left_light, right_light))
if  float(left_light - right_light) <= 0.08 and float(left_light - right_light) >= 0:
    finch.wheels(0.25,0.25)

# If the finch is getting more light in the right than left
elif right_light > left_light:
    print("Going right")
    finch.wheels(0.25,0)
    sleep(1.0)

# If the finch is getting more light in the left than right        
elif left_light > right_light:
    print("Going left")
    finch.wheels(0,0.25)
    sleep(1.0)
    


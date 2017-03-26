from finch import Finch
from time import sleep
finch = Finch()

class OurFinch: # Everything the finch is supposed to do!
  # Initialising
  def init(self):
    finch.led(6, 6, 6)
    finch.buzzer(1.0, 400)
    sleep(0.1)
    finch.buzzer(1.0, 600)
    sleep(0.1)
    finch.buzzer(1.0, 800)
    sleep(0.1)
    finch.buzzer(1.0, 800)
    sleep(0.1)
    finch.buzzer(1.0, 600)
    sleep(0.1)
    finch.buzzer(1.0, 400)
    print('Temperature %5.2f' % finch.temperature())
    sleep(1.5)
    return 1

  # This function checks the temperature of the bodies to see if they are alive!
  def checktemp(self, bodies, bodies_max):
      
      #Print the temperature
      print ('Temperature %5.2f' % finch.temperature())
      #if the temperature is greater than or equal to 10 degrees
      if finch.temperature() >= float ("10.00"):
         #print thats its alive
         print ("IT'S ALIVE!!")
         finch.led("#FF0000") # set the led to red
         finch.buzzer(1, 666) # Buzz
         print ("Before", bodies)
         #Add one to bodies (will later make more sense)
         bodies += 1
         print ("After", bodies)
         sleep(1.5)
         return bodies
      else:
        # If the temperature was less than ten it was just an obstacle
        print ("Nochange")
        sleep(1.5)
        return bodies


  #Function Go Ninja
  def goninja(self, bodies, bodies_max, mode):
      # Get the Z-Axis acceleration
      zAccel = finch.acceleration()[2]
      # Do the following while the Finch is not upside down 
      while zAccel > -0.7:
        # if the mode is exit
          if mode == 'exit':
            sleep (2.0)
            #Then go to function "follow the light"
            self.followthelight()
            
          left_obstacle, right_obstacle = finch.obstacle()
          if (right_obstacle or left_obstacle):
            print ("RIGHT : ", right_obstacle, "::::: LEFT : ", left_obstacle)

          if right_obstacle or left_obstacle:
            finch.wheels(0.0,0.0)
            sleep(0.5)
            # if mode is set to search
            if mode == 'search':
              # and if the bodies is equal to bodies max
              if bodies == bodies_max :
                self.findthelight()
                print ("Going home")
                #set mode to exit
                mode = 'exit'
              else:
                #else go to function to check temp to make sure its a body
                print ("Adding bodies!")
                bodies = self.checktemp(bodies, bodies_max)
            else :
                self.followthelight()
            # If there's an obstacle on the left, back up and arc
            if left_obstacle:
                finch.led(255,0,0)
                finch.wheels(-0.3,-1.0)
                sleep(1.0)
            # If there's an obstacle on the right, back up and arc
            elif right_obstacle:
                finch.led(255,255,0)
                finch.wheels(-1.0,-0.3)
                sleep(1.0)

          # Else just go straight
          else:
              finch.wheels(1.0, 1.0)
              finch.led(0,255,0)
          # Keep reading in the Z acceleration
          zAccel = finch.acceleration()[2]

  # Function follow the light
  def followthelight(self):
    left_light, right_light = finch.light()
    print ('Lights %5.3f, %5.3f' % (left_light, right_light))
    if  float(left_light - right_light) <= 0.08 and float(left_light - right_light) >= 0:
        finch.wheels(1.0,1.0)

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
    

    return
        
  # Search for the brighest point
  def findthelight(self):
    pos   = 0.0
    left  = 0.0
    right = 0.0
    count = 0
    my_pos   = {count:pos}
    my_left  = {count:left}
    my_right = {count:right}
    while (count < 17):
      print ("COUNT : ", count)
      left, right = finch.light()
      finch.wheels(0,0.25)
      sleep(1.0)
      my_left[count] =float(left)
      my_right[count]=float(right)
      my_pos[count]  =float(pos)
      count += 1
      pos += 0.25
    print sorted(my_left.values())
    print('left : ', my_left)
    print('right : ', my_right)
    print('pos : ', my_pos)


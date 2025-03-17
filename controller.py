import  pyfirmata
comport = 'COM8'
board=pyfirmata.Arduino(comport)
import time


len1Green=board.get_pin('d:3:o')
len1Yellow=board.get_pin('d:5:o')
len1Red=board.get_pin('d:7:o')
len2Green=board.get_pin('d:12:o')
len2Yellow=board.get_pin('d:11:o')
len2Red=board.get_pin('d:9:o')


def led(len1totalcounter,len2totalcounter):
   if len1totalcounter > len2totalcounter:
        len1Yellow.write(1)
        len2Yellow.write(1)
        time.sleep(4)
        len1Yellow.write(0)
        len2Yellow.write(0)
        
        if len1totalcounter == 2:
            len1Green.write(1)
            len2Red.write(1)
            time.sleep(5)  # Green for 5 seconds
            len1Yellow.write(1)
            len2Yellow.write(1)
            time.sleep(4)  # Yellow for 4 seconds
        elif len1totalcounter >= 3:
            len1Green.write(1)
            len2Red.write(1)
            time.sleep(10)  # Green for 10 seconds
            len1Yellow.write(1)
            len2Yellow.write(1)
            time.sleep(4)  # Yellow for 4 seconds

        # Turn off lights after respective durations
        len1Green.write(0)
        len2Red.write(0)
        len2Green.write(0)
        len2Yellow.write(0)
        len1Yellow.write(0)
   elif len2totalcounter > len1totalcounter:
        # Lane 2 has more cars
        len1Yellow.write(1)
        len2Yellow.write(1)
        time.sleep(4)
        len1Yellow.write(0)
        len2Yellow.write(0)

        if len2totalcounter == 2:
            len2Green.write(1)
            len1Red.write(1)
            time.sleep(5)  # Green for 5 seconds
            len1Yellow.write(1)
            len2Yellow.write(1)
            time.sleep(4)
             
        elif len2totalcounter >= 3:
             len2Green.write(1)
             len1Red.write(1)
             time.sleep(10)  # Green for 10 seconds
             len2Yellow.write(1)
             len1Yellow.write(1)
             time.sleep(4)  # Yellow for 4 seconds

        # Turn off lights after respective durations
         
        len2Green.write(0)
        len1Red.write(0)
        len1Green.write(0)
        len1Yellow.write(0)
        len2Yellow.write(0)


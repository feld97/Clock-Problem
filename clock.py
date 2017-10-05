# The Clock problem

# Your must write a program, in Python, which reads in a file.  This file will have a number of digital clock times, one per line,
# which should be of the form: "hour:minute" for any valid digital time, civilian or military.  For each time your program should:
#
#       * If the time is an invalid time, print "ERROR"
#       * If the time is a valid time, build an abstract representation of a clock with a minute hand and an hour hand and print the smallest angle between these two hands for the time in question.
#
# Create a github repository and include both your code, and evidence of testing your program.  Share this repository with Dr. Rozier.


file_name = input('Enter the name of the file: ')
try:
    if (file_name.endswith('.txt')):
        file_in = open(file_name, "r")
    else:
        file_in = open(file_name + '.txt', "r")
except FileNotFoundError as e:
    print("I cannot find that file!")
    exit()

print()
for line in iter(file_in):
    try:
        hours = int(line.split(":")[0])
        minutes = int(line.split(":")[1])
        if(minutes > 59 or minutes < 0 or hours < 0 or hours > 24 or len(line.split("\n")[0]) > 5):
            raise ValueError
        # build clock here

        # convert both to degrees
        # hours/12   = x/360 or x = hours * 30
        # minutes/60 = x/360 or x = minutes*6
        hDegrees = (hours%12) * 30
        mDegrees = minutes    * 6

        difference = abs(hDegrees-mDegrees) if abs(hDegrees-mDegrees) < 180 else 360-abs(hDegrees-mDegrees)

        print("'"+line.split("\n")[0]+"', Hour hand is at " + str(hDegrees)+ " degrees, and Minute hand is at "+str(mDegrees)+" degrees")
        print("the smallest angle between is " + str(difference) + " degrees")
        print()

    except Exception as e:
         print("ERROR")
         print()

file_in.close()

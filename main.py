# argv.py
import sys
import numpy as np

curveType = str(sys.argv[1:])  #read in argument from terminal
curveType = curveType.replace("['", "")  #clean up text
curveType = curveType.replace("']", "")  #clean up text
if curveType == "":  #failsafe if nothing is entered just do the standard RIAA curve.
    curveType = "0"
#curveType is a parameter to use while generating output, 0 would be standard RIAA playback curve, 1 would
#be IEC RIAA curve, 2 and on are to be determined.
sampleRates = [22050, 24000, 44100, 48000, 96000] #common sampling rates halved to represent actual frequencies
t1 = 0.00318
t2 = 0.000318
t3 = 0.000075
t4 = 0.00795
pi = 3.14159265358979323846264338327950 #excessive number of digits of pi due to knowledge of too many digits.
for j in range(0, len(sampleRates)):
    if curveType.isdigit() is False:  #stop program before a non digit is checked in the inner for loop.
        print("Non supported entered.")
        break
    for i in range(20, sampleRates[j]+1): #start at 20 to prevent amplification of subsonic frequenies
        # file written to is in format frequency, amplitude.
        #formula for RIAA curve and IEC RIAA curve found at https://www.bonavolta.ch/hobby/en/audio/riaa.htm
        if curveType == "0":
            f = open(("riaa" + str(sampleRates[j]) +".csv"), "a")
            f.write(str(i))
            f.write(", ")
            first = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t2, 2)))))
            second = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t1, 2)))))
            third = 10*(np.log10(1+4*np.power(pi, 2)*np.power(i, 2)*np.power(t3, 2)))
            amp = str(first-second-third)
            f.write(amp)
            f.write("\n")
            f.close()
        elif curveType == "1":
            f = open(("iecRIAA" + str(sampleRates[j]) +".csv"), "a")
            f.write(str(i))
            f.write(", ")
            first = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t2, 2)))))
            second = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t1, 2)))))
            third = 10*(np.log10(1+4*np.power(pi, 2)*np.power(i, 2)*np.power(t3, 2)))
            fourth = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t4, 2)))))
            amp = str(first-second-fourth-third)
            f.write(str(amp))
            f.write("\n")
            f.close()
        else:
            print("Non supported input entered.")  #this will cover curveType values that aren't yet supported, like 2, 3, 42, etc.
            break

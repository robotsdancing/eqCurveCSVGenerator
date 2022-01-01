import numpy as np

curveType = "0" #curveType values: 0 = RIAA curve,  1 =
sampleRates = [22050, 24000, 44100, 48000, 96000] #common sampling rates halved to represent actual frequencies
t1 = 0.00318
t2 = 0.000318
t3 = 0.000075
t4 = 0.00795
pi = 3.14159265358979323846264338327950 #excessive number of digits of pi due to knowledge of too many digits.
for j in range(0, len(sampleRates)):

    for i in range(20, sampleRates[j]+1): #start at 20 to prevent amplification of subsonic frequenies
        # file written to is in format frequency, amplitude.
        f = open(("riaa" + str(sampleRates[j]) +".csv"), "a")
        f.write(str(i))
        f.write(", ")
        #formula found at https://www.bonavolta.ch/hobby/en/audio/riaa.htm
        first = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t2, 2)))))
        second = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t1, 2)))))
        third = 10*(np.log10(1+4*np.power(pi, 2)*np.power(i, 2)*np.power(t3, 2)))
        fourth = 10*(np.log10(1+(1/(4*np.power(pi, 2)*np.power(i, 2)*np.power(t4, 2)))))
        amp = str(first-second-third)
        f.write(amp)
        f.write("\n")
        f.close()
        f = open(("iecRIAA" + str(sampleRates[j]) +".csv"), "a")
        f.write(str(i))
        f.write(", ")
        amp = str(first-second-fourth-third)
        f.write(str(amp))
        f.write("\n")
        f.close()

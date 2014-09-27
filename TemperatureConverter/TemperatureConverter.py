__author__ = 'Derek'
# A simple program to convert temperatures from celsius to fahrenheit or vice versa

def convert(temp, conversion):
    if conversion == 'F':
        tempF = (9/5.0)*temp+32
        return tempF
    else:
        tempC = (5/9.0)*(temp-32)
        return tempC

print "Temperature Converter\n"

tempIn = int(raw_input("Enter a temperature: "))
conversionType = raw_input("Convert to (F)ahrenheit or (C)elsius: ")
conversionType = conversionType.upper()

if conversionType == 'F':
    otherConversionType = 'C'
else:
    otherConversionType = 'F'

print '{} {} = {} {}'.format(tempIn, otherConversionType, convert(tempIn,conversionType),conversionType)
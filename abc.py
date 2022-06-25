print('Welcome to ELEARN BMI CALCULATOR')
print('**************************************************')

print('Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. Use the tool below to compute yours.')

print('')

print('----BMI Categories---')
print('Underweight = <18.5')
print('Normal weight = 18.5–24.9')
print('Overweight = 25–29.9')
print('Obesity = BMI of 30 or greater')

print('')

Height=float(input("Enter your Height in Centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))

#BMI formular is BMI=kg/m**2
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)

if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("You are overweight")
	else: print("You are severely overweight")
else:
    print('Enter Your Details here')
    name=input('Enter your Name: ')
    phone=input('Enter your Phone Number: ')
    print('Thanks')
   


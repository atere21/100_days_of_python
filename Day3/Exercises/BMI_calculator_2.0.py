# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#float() converts strings into floating point numbers
BMI = round (weight / height ** 2)

if(BMI < 18.5):
  print(f"Your BMI is {BMI}, you are underweight.")
elif(BMI >= 18.5 and BMI < 25):
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif(BMI >= 25 and BMI < 30):
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif(BMI >= 30 and bmi < 35):
    print(f"Your BMI is {BMI}, you are obese.")
elif(BMI > 35):
    print(f"Your BMI is {BMI}, you are clinically obese.")
    
# Note: Be careful of the sample input, as it has height and weight swapped from code produced from editor. 

# Code to Calculate Bmi
gender_input=str(input("enter your gender, all small letters"))
weight_input=float(input("enter you weight in kilogram"))
height_input=float(input("enter your height in metres"))
Bmi=weight_input/(height_input**2)
if gender_input == "male" and 18.5<=Bmi<25.0:
    print("Your Bmi which is", round(Bmi, 2), "is" "normal weight")
elif gender_input =="male" and 25<=Bmi<29:
    print("Your Bmi which is", round(Bmi, 2), "is" "overweight")
elif gender_input =="male" and Bmi>30:
    print("Your Bmi which is", round(Bmi, 2),"is" "obese")
elif gender_input =="male" and Bmi<18.5:
    print("Your Bmi which is", round(Bmi, 2), "is" "underweight")

if gender_input == "female" and 18.5<=Bmi<25.0:
    print("Your Bmi which is", round(Bmi, 2), "is", "normal weight")
elif gender_input == "female" and 25<=Bmi<30.0:
    print("Your Bmi which is", round(Bmi, 2), "is", "overweight")
elif gender_input == "female" and Bmi>30.0:
    print("Your Bmi which is", round(Bmi, 2), "is", "Obese")
elif gender_input == "female" and Bmi<18.5:
    print("Your Bmi which is", round(Bmi, 2), "is", "Obese")
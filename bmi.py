height = float(input("what is your height in meters? "))
weight = float(input("what is your body weight in kilograms? "))
bmi = weight/(height**2)
if bmi < 18.3:
    print(f"{bmi:.1f},偏瘦")
elif bmi < 24:
    print(f"{bmi:.1f},正常")
elif bmi <28:
    print(f"{bmi:.1f},超重")
else:
    print("肥胖")
from datetime import datetime, date
#Title of page
print('\t\t\t BMI Calculator')
print("Please select a option")
print("1. continue  2. Exit \n")
user_menu_option = str(input(("Please enter a value: ")))


while user_menu_option == '1':

    user_name = input("Please enter your name: ")
#calculates the age of the user by DoB
    date_of_birth = datetime.strptime(input("Your date of birth (dd mm yyyy): "), "%d %m %Y")

    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    age = calculate_age(date_of_birth)

    if age <= 18:
        user_input_sex = input("Are you Male or Female: ").lower()
        print("Please select a wight method.")
        user_input_measurement = str(input("1. Metric 2. Imperial: "))

        if user_input_measurement >= '3':
            print("Try agin")
            break


        if user_input_measurement == '1':
            hight = float(input("please enter Your hight in meters: "))
            weight = int(input("Please enter your weight in KG: "))

            bmi = round(weight/(hight*hight), 1)
            print(bmi)

            if bmi <= 18.5:
                print("Your BMI is", bmi, "which means you are underweight.")
            
            elif bmi > 18.5 and bmi < 25:
                print("your BMI is", bmi, 'which means you are normal.')

            elif bmi > 25 and bmi < 30:
                print('your BMI is', bmi, 'which means you are overweight.')

            elif bmi > 30:
                print('Your BMI is', bmi,'which means you are obese.')

            input("Please enter (Y) if you would like to enter another BMI, if no press enter: ")


    if user_input_measurement == '2':

        height = int(input('Please enter your height input Inches(whole number): '))
    weight = int(input('Please enter your weight input pounds(whole number): '))
    bmi = round((weight*703)/(height*height), 1)

    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi,'which means you are overweight')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    input("Please enter (Y) if you would like to enter another BMI, if no press enter: ")
else:
    print("Please Try again")



            



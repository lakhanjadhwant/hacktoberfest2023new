def calculate_bmi(weight_kg, height_m):
    try:
        bmi = weight_kg / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def interpret_bmi(bmi):
    if isinstance(bmi, str):
        return bmi
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    result = interpret_bmi(bmi)

    if isinstance(bmi, str):
        print(result)
    else:
        print(f"Your BMI is {bmi:.2f}, which is considered '{result}'.")

if __name__ == "__main__":
    main()

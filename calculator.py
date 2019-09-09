def check_LDL(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result < 159:
        return "Borderline high"
    elif 160 < LDL_result <= 189:
        return "High"
    elif LDL_result > 190:
        return "Very High"

def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline low"
    else:
        return "low"

def cholesterol_interface():
    print("Cholesterol check")
    chol_input = input("Enter your cholesterol test results: ")
    chol_data = chol_input.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(int(chol_data[1]))
        print("The result is {}".format(result))
    elif chol_data[0] == "LDL":
        result2 = check_LDL(int(chol_data[1]))
        print("The result is {}".format(result2))

def interface():
    print("My calculator program")
    keep_running = True
    while keep_running:
        print("Option: ")
        print("1 - Cholesterol Check")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            cholesterol_interface()
    return

if __name__ == "__main__":
    interface()

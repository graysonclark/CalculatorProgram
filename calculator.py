def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline low"
    else:
        return "low"

def cholesterol_interface():
    print("Cholesterol check")
    chol_input = input("Enter your cholesterol test results: ")
    chol_data = chol_input.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(chol_data[1])
        print("The result is {}".format(result))
def interface():
    print("My calculator program")
    keep_running = True
    while keep_running:
        print("Option: ")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            keep_running = False
    return

if __name__ == "__main__":
    interface()

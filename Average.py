# Function to calculate the average of 3 scores
def calc_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

# Function to evaluate status based on grading rules
def get_status(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 80:
        return "Very Good"
    elif avg >= 75:
        return "Passed"
    else:
        return "Failed"

# Get number of students
total_students = int(input("How many students? "))

# Input check to meet assignment rule of at least 3 students
if total_students < 3:
    print("Notice: Setting student count to minimum of 3.")
    total_students = 3

# Main loop to input and display student records
for i in range(1, total_students + 1):
    print(f"Student {i}")
    name = input("Enter name: ")
    
    act1 = float(input("Activity 1: "))
    act2 = float(input("Activity 2: "))
    act3 = float(input("Activity 3: "))
    
    # Processing
    average = calc_average(act1, act2, act3)
    status = get_status(average)
    
    # Display output
    print(f"Average: {average:.2f}")
    print(f"Status: {status}\n")

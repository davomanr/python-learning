# -------------------------------
# Student Score Analyzer
# -------------------------------

# Ask the user how many students' scores they want to enter
num_students = int(input("Enter the number of students: "))

# Create an empty list to store all the scores
scores = []

# Use a loop to collect scores one by one
for i in range(num_students):
    # Ask for each student's score
    # input() always gives text, so we use int() to convert it into a number
    score = int(input(f"Enter score for student {i + 1}: "))

    # Append (add) each score to the list called 'scores'
    scores.append(score)

# -----------------------------------
# PROCESSING PART
# -----------------------------------

# Calculate the average score
average_score = sum(scores) / len(scores)

# Find the highest score in the list
highest_score = max(scores)

# Find the lowest score in the list
lowest_score = min(scores)

# -----------------------------------
# OUTPUT PART
# -----------------------------------

# Print all the scores entered
print("\nAll scores:", scores)

# Print the calculated results
print(f"Average Score: {average_score:.2f}")  # .2f rounds to 2 decimal places
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

# Optional feedback message
if average_score >= 90:
    print("Excellent performance! 🎯")
elif average_score >= 75:
    print("Good job! Keep it up 👍")
else:
    print("Needs improvement. You can do it! 💪")

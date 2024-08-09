# Welcome Message: Display a welcome message to the user.

print("***********************************************")
print("Welcome to my quiz game!!!")


# create a qestion bank data list which has multiple dictionary that includes 2 key and value pairs
#  text as Key and questions as Values, 
# similarly another key and value pair as answer and correct option
question_bank=[
    {"text" : "how many bones does human body have?", "answer": "A"},
    {"text" : "Which is the hottest planet in the solar system?", "answer": "D"},
    {"text" : "Which animal lays the biggest egg?", "answer": "C"},
    {"text" : "Which is the highest peak in the world?", "answer": "C"},
    {"text" : "What is the capital of France?", "answer": "B"}
]

# creating a list and sublist for the options to choose
options=[["A. 206", "B. 207", "C. 208", "D. 210"],
         ["A. Mercury", "B. Mars", "C. Saturn", "D. Venus"],
         ["A. Elephant", "B. Whale", "C. Ostrich", "D. Tortorise"],
         ["A. Kilimanjaro", "B. K2", "C. Mount Everest", "D. Kangchenjunga"],
         ["A. Germany", "B. Paris", "C. Italy", "D. Berlin"]
]
score =0
def check_answer(user_guess, correct_answer): #define function with 2 args
 if user_guess==correct_answer:
    return True
 else:
    return False

# to print the question, using the range function where the range should be till the length of questionbank
for question_num in range(len(question_bank)):
    print("**************************************************")
    print(question_bank[question_num]["text"]) 
    for i in options[question_num]:  # we have to provide question num inorder give the matching question and option
        print(i)

    guess = input("Enter your answer(A/B/C/D): ").upper()    # created user input - answer from the user
    
    # check answer of user using the function and pass the user input and correct option with the Key value pair answer selected
    is_correct = check_answer(guess,question_bank[question_num]["answer"]) 
    if is_correct:
       print("correct answer")
       score +=1
    else:
       print("incorrect answer")
       print(f"the correct answer is {question_bank[question_num]['answer']}")

    print(f"your current score is{score}/{question_num+1}")

print(f"yur final score is {score}")
print(f"your score is {(score/len(question_bank))*100}%")




 


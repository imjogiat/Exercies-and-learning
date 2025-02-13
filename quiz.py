import json

with open("quiz_questions.json","r") as file:
    content = file.read()

data = json.loads(content)
score = 0

for question in data:
    user_choice = input(f"\n\n{question["question_text"]}\n\n{question["choices"]}\n\n")

    user_choice = user_choice.title()
    user_choice = user_choice.strip()

    correct_number = question["correct_answer"]
    

    if user_choice == question["choices"][correct_number-1]:
        print("That's correct")
        score = score + 1
    
    else:
        print("You're wrong")
    
print(fr"Youre score is {score}/{len(data)}")

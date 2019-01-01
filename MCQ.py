
from Question import Question
question_prompts=[
    "What color are apples? \n (a) red/green \n(b) indigo \n(c) blue\n\n",
    "What color are banana? \n (a) magenta \n(b) teal\n(c) yellow\n\n",
    "What color are coconut? \n (a) Brown \n(b) gold\n (c) silver\n\n"
]

#create array of questions
questions =[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"a"),

]
#Next step write a function that will run the test
def run_test(questions): #one parameter- list of question objects : ask the user(wanna loop/check/track score)
    score=0 #increment the score variable every time the student gets question right
    for question in questions: #for each question object inside of the questionsarray
        #ask user a question and store it inside a variable
        answer=input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got" + str(score) + "/" + str(len(questions)) + " Correct" )

#call this run test function
run_test(questions)





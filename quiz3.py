Questions = {
    "When was the first known use of the word 'quiz'?":["1981", "1987", "2005","1789"],
    "which built in function can get information for us ?": ["input","format","output"]

}

for question, alternatives in Questions.items():
    rightanswer = alternatives[0]
    for choices in alternatives:
        print(" -{}".format(choices))



    answer = input(question)

    if answer== rightanswer:
        print("correct")
    else:
        print("The answer is {}, not {}".format(rightanswer,answer))


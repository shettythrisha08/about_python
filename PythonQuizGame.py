#python quiz game
questions=("which keyword is used to define a constant in c",
           "what is the output of print (type(10))in Python",
           "which data structure follows FIFO",
           "which symbol is used to access structure members in C:")

options=(("A.var","B.let","C.const","D.define"),
         ("A.<class 'float'>","B.<class 'int'>","C.<class 'str'>","D.<class 'bool'>"),
         ("A.Stacks","B.Queues","C.Trees","D.Graphs"),
         ("A.:","B..","C.->","D.#"))

answers=("C","B","B","B")
guesses=[]
score=0
question_number=0


for question in questions:
    print("-------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess=(input("Enter(A,B,C,D):")).upper()
    guesses.append(guess)
    if guess== answers[question_number]:
        score+=1
        print("correct anser!!!,nailed it queen")
    else:
        print(f"o No wrong answer!!the correct answer is {answers[question_number]}")
    question_number+=1
print("------------------------------------------")
print("RESULT")
print("------------------------------------------")
percentage=score/4*100
print(f"your score  is {percentage} %")
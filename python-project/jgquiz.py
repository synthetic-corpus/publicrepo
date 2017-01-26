from random import randint
import string

#This is the final project for stage 2.
#Subject is 'Movie Quotes for Millenials!!'
#Gets harder the older the Movie!!
#All code is original to me (Joel Gonzaga). Additional help from udacity forums
# and the rest of the udacity Python course.

###----Objective / Global Value Section ----
## Contians lists, dictionaries etc, that will be manipulated by functions
## Most will be constant throughought the running of the functions.

#Giant Dictionary below. Contains question id (aka 'qid'), question text, answers etc
#Quizlist Data Sturcture:
#     {question ID :{question and answer}}
#Question and Answer data Structure:
#     {question:'question text', answer:[list of possible answers],}

#simple score list. Must equal length of five to get the "win" message.
score = []

#Movies from 2000s
easy = {
'the Village (2004)':{'q':"'There are _____ in every corner of this Village. Do you not feel it?' -Joaquin Phoenix",'a':['secrets']},
'Batman Begins (2004)':{'q':"'_____ does not wait for you to be ready! _____ is not conisderate nor fair!' -Liam Neeson",'a':['death']},
'Superbad(2007)':{'q':"This is our last party as _____ people. I fully ignored my hatred for Becka in coming up with this plan.' -Jonah Hill",'a':['high school','highschool']},
'the Last Samurai (2003)':{'q':"'I have introduced myself. You have introduced yourself. This is a very good _____.' - Ken Wantanbe'",'a':['conversation']},
'Tropic Thunder (2008)':{'q':"'I know who I am! I'm the _____ playin' the _____, disguised as another _____!' -Robert Downey Jr",'a':['dude','dood']}
}

#Movies from 1990s
medium = {
'subUrbia (1996)':{'q':"Nothing ever changes, man. Fifty years from now we're all gonna be dead. And there will be another group of people standing here drinking beer, eating pizza, bitching about the price of _____...' -Giovanni Ribisi'",'a':['oreos']},
'the Usual Suspects (1995)':{'q':"'Who is _____? He is supposed to be Turkish. Some say his father was German. Nobody believed he was real. Nobody ever saw him or knew anybody that ever worked directly for him' -Kevin Spacey",'a':['keyser soze','kaiser soze','keyzer soze']},
'clockwatchers (1997)':{'q':"'The only real challenge with this job, is trying to _____ when there's nothing to do.' -Parker Posey",'a':['look busy']},
'the Matrix (1999)':{'q':"'Have you ever had a _____, Neo, that you were so sure was real? What if you were unable to wake from that _____?' -Laurence Fishburne",'a':['dream']},
'the Crow (1994)':{'q':"'_____ is the name for God on the lips and hearts of all children.' -Brandon Lee",'a':['mother','mom','mommy']}
}

#Movies from the 1980s
hard = {
'the Lost Boys(1987)':{'q':"'Now you know what we are, now you know what you are. You'll never grow old, Michael, and you'll _____.' -Keifer Sutherland",'a':['never die']},
'Say Anything (1989)':{'q':"'I don't want to sell _____, buy _____, or process _____ as a career...you know, as a career, I don't want that.' -John Cusak",'a':['anything']},
'Kung Fury (2015)':{'q':"'I'm a cop, and damn good at my job. It all began years ago, in the line of duty. Me and my partner were chasing down a mysterious _____.' -David Sandberg",'a':['kung fu master','kungfu master']},
'Ghostbusters (1984)':{'q':"'Everything was fine with our system until the power grid was shut off by _____ here.' -Dan Aykroyd",'a':['dickless','dick less']},
'Back to the Future (1985)':{'q':"_____? Where we're going, we don't need _____.' -Christopher Lloyd",'a':['roads']}
}

#quiz dictionary will be filled with a copy of one the above.
quiz = {}
#Matches string value user input to name of dictionary list.
level_names = {'easy':easy,'medium':medium,'hard':hard}

#This list will be used to keep question in Random order.
randomizer = []

### ----Fuction Section----

#This Fuctions takes user input, question string, and returns the combined string.
#All Blanks must me '_____' for this to work right.
def fillBlank(userstring,question):
    replaced = question.replace("_____",userstring)
    return replaced

#Run by User to Select Level
#Tested and works as expected.
#Returns a string used for reader feedback only.
def select():
    acceptableChar = ['easy','medium','hard']
    inputGood = False
    while not inputGood:
        print "*** Select Level easy, medium, or hard: "
        l = raw_input()
        if l in acceptableChar:
            inputGood = True
    quiz.update(level_names[l])
    if l == 'easy':
        return "2000s"
    if l == 'medium':
        return "90s"
    if l == 'hard':
        return '80s'


#Use to present the quiz question in a random order.
def makeRandom(q_list):
    for e in q_list:
        randomizer.append(e)

#This is an input check.
#Will return True or False.
#User input should be letters and spaces only.
#User Input should be at least 4 characters.
def inputcheck(input):
    #Letters and spaces are only good input.
    s = input.lower()
    if len(s) < 4:
        return False
    charset = string.ascii_lowercase + "    "
    for c in s:
        if c not in charset:
            return False
    return True

#Grades the user answers.
def gradeQuestion(reply,qid):
    #Extra search strings to allow for more flexible written answers.
    #Grade Question Needs to Return True or False only.
    answers = quiz[qid]['a']
    if reply.lower() in answers:
        return True
    return False

## This asks a question, checks with gradeQuestion().
##Sets "Game Over" condition (Return False) after three wrong answers.
#Tested and works as Expected.
def askquestion(qid):
    tries = 0
    isCorrect = False
    while not isCorrect:
        #Input Validation.
        isGood = False
        while not isGood:
            print "*** "
            print "*** Fill The Blank:"
            print "*** " + quiz[qid]['q']
            print "Answer: "
            reply = raw_input()
            if inputcheck(reply):
                isGood = True
            else:
                print "*** Letters only"
                print "*** at Least four characters"
        #Correct Answer Condition
        if gradeQuestion(reply,qid):
            isCorrect = True
            score.append("correct")
            #Will add this later
            print "*** "
            print "*** Your Answer:"
            print "*** " + fillBlank(reply,quiz[qid]['q']) + " from " + qid
            return True
        #Wrong answer entered. Loop begins agian. Tries iterates.
        else:
            tries += 1
            print "***"
            print "*** Try Again... Strike: ",tries
        #Returns 'False' if Three Tries attempted.
        #This is the Game Over Condition.
        if tries == 3:
            print "***"
            return False

#Takes in a the randomizer list.
#Loops through questions.
#Returns game over if game over.
def questionLooper(randomizer):
    while len(randomizer) > 0:
        index = randint(0,len(randomizer)-1)
        nextq = randomizer.pop(index)
        #Asks question. Checks for correct answer.
        #Checks for Game Over condition is met.
        if not askquestion(nextq):
            print "*** Game Over."
            break
        else:
            if len(randomizer) > 0:
                print "***"
                print "*** Good job! Next Question..."

#Run Quiz This is the function that actually runs the quiz
def run_quiz():
    #Quiz intro.
    print "*** Movie Trivia Game For Millenials!"
    print "*** Can our limited attention span remember previous decades?!"
    print "*** Select your difficultly level to find out!"
    print "***"
    #Run Selection function
    #'Decade' variable is for feedback only.
    decade = select()
    #Run Randomize function
    makeRandom(quiz)
    #Run The ask Questions Loop
    questionLooper(randomizer)
    #quizfeedback
    if len(score) == 5:
        print "***"
        print "***Great job, you really know your "+ decade +" movies!!"
    else:
        print "*** Please try again."

run_quiz()

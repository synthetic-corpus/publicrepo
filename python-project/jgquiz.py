from random import randint
import string
#This is the final project for stage 2.
#Subject is philosophy.
#All code is original to me (Joel Gonzaga). Additional help from udacity forums
# and the rest of the udacity Python course.


#Score = P{{ stores the question id (qid) and mark 0 or 1 if good.
#Data Structure
#    {'qid':zero or one}
#Initialized as an empty dictionary. To be updated by gradeQuestion()
score = {}

#Giant Dictionary below. Contains question id (aka 'qid'), question text, answers etc
#Quizlist Data Sturcture:
#     {question ID :{question and answer}}
#Question and Answer data Structure:
#     {question:'question text', answer:[list of possible answers],'e':'Explanation of correct answer'}
quizlist = {
'kant':{'q':"Kant's moral maxim was '______ implies can.'",'a':['ought'],'e':"Kant said 'ought implies can.'"},
'platonism':{'q':"In Plato's 'Republic,'' who was in charge? The Alphas, the Philosopher kings, or the Craftsmen?",'a':['philosophers','philosopher king','philosopher guardian'],'e':"The leaders of the republic were known as 'Philosopher Kings'"},
'socrates':{'q':"Name one of the four famous dialouges form 'The Trial and Death of Socrates.'",'a':['apology','crito','euthyphro','phaedo'],'e':"the Dialouges were, 'Apology, Crito, Euthyphro, and Phaedo.'"},
'cogito':{'q':"Who wrote the words 'Cogito Ergo Sum'?",'a':['descartes','rene descartes','some french guy with a big nose'],'e':"Rene Descartes is famous for 'Cogito Ergo Sum' aka 'I think therefore I am.'"},
'sartre':{'q':"Which philosopher and playwright said 'hell is other people'?",'a':['sartre','jean paul sartre'],'e':"In his play 'no exit', Sartre's main character declares 'Now I know what Hell is. Hell is other people.'"},
'james':{'q':"Founder of a uniquely American school of philosophy. Wrote 'Varieties of Religious Experience'",'a':['who is william james','will jamess','william james','billy james'],'e':'William James, father of pragmatism'},
'neitzsche':{'q':"Great German philosopher who loved Lou Salome like Snape loved Lily. Died equally obsessed and a bit more crazy.",'a':['neitzsche','nietzsche','neitzche','neetschey'],'e':"Lou Salome rejected Friedrich Nietzsche so hard that he had to invent a whole new type of existentialism."}
}
#This list will be used to keep question in Random order.
randomizer = []
for e in quizlist:
    randomizer.append(e)

#This is an input check.
#Will return True or False.
#User input should be letters and spaces only.
def inputcheck(input):
    #Letters and spaces are only good input.
    s = input.lower()
    if len(s) <4:
        return False
    charset = string.ascii_lowercase + "    "
    for c in s:
        if c not in charset:
            return False
    return True

#Grades the user answers.
#Stores answers in Score dictionary.
def gradeQuestion(reply,qid):
    #Extra search strings to allow for more flexible written answers.
    answers = quizlist[qid]['a']
    correct = False
    for e in answers:
        if e.find(reply.lower()) != -1:
            correct = True
    if correct:
        score.update({qid:1})
    else:
        score.update({qid:0})

## This asks a question, takes in the answer, and validates the input.
def askquestion(qid):
    isGood = False
    while not isGood:
        print quizlist[qid]['q']
        print "Answer: "
        reply = raw_input()
        if inputcheck(reply):
            isGood = True
        else:
            print "Input not good. Letters and Spaces only."
            print "Input must be at least four characters."
    gradeQuestion(reply,qid)

#Run Quiz This is the function that actually runs the quiz
def run_quiz():
    #Ask questions. Randomly ordered.
    print "*** Welcome to Philosophy Trivia!"
    print "*** Answer in letters only. No leading or trailing spaces."
    print "*** Start Quiz!"
    while len(randomizer) > 0:
        index = randint(0,len(randomizer)-1)
        nextq = randomizer.pop(index)
        askquestion(nextq)
    #Calculates Score
    total = 0
    for q in score:
        total = total + score[q]
    #Gives user Feedback
    print "*** Quiz Finished!"
    print "*** Score is ",total," out of ",len(quizlist)
    print "*** Question Review"
    print ""
    for qid in score:
        if score[qid] == 1:
            print "*** Question: " + quizlist[qid]['q']
            print "*** Your answer was CORRECT!!"
            print "*** Explanation: " + quizlist[qid]['e']
            print ""
        else:
            print "*** Question: " + quizlist[qid]['q']
            print "*** Your answer was INCORRECT..."
            print "*** Explanation: " + quizlist[qid]['e']
            print ""
run_quiz()

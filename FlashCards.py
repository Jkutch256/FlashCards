import random 
import json 
questions = {" what is the first element?": "Hydrogen", 
             " what is the second element?": "helium", 
             " what is the third element?": "Lithium", 
             " What is the fourth element?": "Beryllium", 
             " Who was the 30 president?": "Calvin Coolidge",
             " What is the 10th element?" : "Neon", 
             " Who was the first president": "George Washitgon", 
             " What is the 28 element?": "Nickel", 
             " What is the 42 element?": "molybdenum", 
             " What is the 67 element?": "Holmium",
             " What is the 32 element?": "Germanium",
             " What is the 6 element?": "Carbon",
             " What is the 13th element?": "Aluminum",
             " What is the 14th element?": "Silicon",
             " what is the 16th element?":"Sulfur",
             " What is the 15th element": "Phosphorus",
             " what is the 17th element?": "Chlorine",
             " What is the 18th element": "Argon",
             " What is the 19th element": "Potassium",
             " what is the 20th element": "Calcium"}

List_new_correct = []
List_incorrect= []


user_questions = list (questions.keys ())
while True: 
     user_question = input ("Do you want a Flash card?:")
     if user_question == "Yes":
            question = random.choice (user_questions)
            user_answer= questions [question]
     else:
             break 
     while True:
        user_response = input (question)
        if user_answer== user_response:
                        print ("You Are correct!!!")
                        List_new_correct.append (question)
                        break
                        
        else:
                        print ("You are incorrect")
                        List_incorrect.append (question)
                        

        
with open ("correct.answer", "w") as f:
      json.dump (List_new_correct,f)
with open ("incorrect.answer", "w") as f:
        json.dump (List_incorrect,f)




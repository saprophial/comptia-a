from Tkinter import *
def QuizWindow(question, answer):

    def ans_reveal():
        answer_text.config(text=answer)
        reveal_button.destroy()
        continue_button = Button(root, text="Next Question", command=close_window)
        continue_button.grid(row=4, column=0,  columnspan=2)

        correct_box.grid(row=3, column=0, sticky=E)
        
        incorrect_box.grid(row=3, column=1, sticky=W)
        

    def close_window():
        # Get return
        """if not (correct_var.get() or incorrect_var.get):
            print "CHECK A BOX!!"
        if correct_var.get() == 1:
            print "Got it right!"
            score =  True     #To signify a Correct score point
        else:
            score = False"""
        root.destroy()
        root.quit()

    def quit_button():
        import sys
        root.destroy()
        root.quit()
        sys.exit()
        

    root = Tk()
    
    question_label = Label(root, text=question)
    question_label.grid(row=0, column=0, columnspan=2, padx=(15, 15))

    answer_text = Label(root, text='')
    answer_text.grid(row=1, column=0, columnspan=2, padx=(15, 15))

    reveal_button = Button(root, text="Reveal Answer", command=ans_reveal)
    reveal_button.grid(row=3, columnspan=2, column=0)

    quit_button = Button(root, text='Quit', command=quit_button)
    quit_button.grid(row=4, columnspan=2, column=0)

    correct_var = IntVar()
    correct_box = Checkbutton(root, text='Correct', variable=correct_var)

    incorrect_var = IntVar()
    incorrect_box = Checkbutton(root, text='Incorrect', variable=incorrect_var)

    root.mainloop()

    return correct_var.get()
    
root_dir = '/home/somzu/Documents/CompTIA/A_Certification/'
note_file = '%sChapter 3 Notes' % root_dir

with open(note_file) as f:
    all_text = f.read().splitlines()
all_text = [x for x in all_text if x]

""" Split up all questions """
#all_questions = all_text.split(';;;')
all_questions = all_text

""" Make a random list of indices to randomize the questions """
from random import shuffle
num_questions = len(all_questions)
all_indices = [i for i in range(num_questions)]
shuffle(all_indices)

score = {
        'Correct' : 0,
        'Incorrect' : 0
        }
print "Beginning %s questions!" % len(all_indices)
review_list = {}
""" Start going through all questions """
for i in all_indices:
    question = all_questions[i]
    # Single and multiple-choice answers should always have the answer ar index 1
    q_split = question.split('*')
    try:
        answer = q_split[1]
    except:
        print "PROBLEM!!!", q_split
        continue
    q_split.pop(1)
    if len([x for x in q_split if x]) > 1:
        question = ' ____ '.join(q_split)
    else: 
        question = ''.join(q_split)
    split_answer = answer.split(';')
    multi_choice = answer.split('/')

    """ Is it a multiple-answer question? """
    if len(split_answer) > 1:
        num_answers = len(split_answer)
        question = "%s (%s answers) " % (question, num_answers)
        answer = ", ".join(split_answer)
    
    result = QuizWindow(question, answer)   
    print result
    if result == 1:
        score['Correct'] += 1
    else:
        score['Incorrect'] += 1
        review_list[question] = answer
        
    print "Score:"
    print "Correct: %s" % score['Correct']
    print "Incorrect: %s" % score['Incorrect']

    #elif len(multi_choice) > 1:
        #for i in range(0, len(multi_choice)):
            #print "%s. %s" % (i, multi_choice[i]


    # ADD A FUNCTION TO GET THE LIST OF WRONG ANSWERS
    with open('%sreview_file_ch3.txt' % root_dir, 'w+') as f:
        for q in review_list.keys():
            f.write('%s\n' % q)
            f.write('%s\n' % review_list[q])
            f.write("\n")
    





























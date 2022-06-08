# function

# text foramatter
# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def yes_no(question_text):
    while True:

        # ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes program continues
        if answer == "yes" or answer == "y":
            answer = "yes"
            return answer

        # if user says no show instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # othwerwise show error
        else:
            print("please answer 'yes' or 'no'")

# function to show instructions



def instructions():

    print(formatter('*', 'how to play'))
    print()
    print( "when you see a number in english answer with the Maori equivalent. For example:\n" 
         "if it showed up with number one you would respond wtih tahi \n"
          "if it came up with 3 you wound say toru.\n")

    print()
    print()

# main routine


played_before = yes_no("have you played the game before? ")

if played_before == "No":
     instructions()
else:
    print("program continues")













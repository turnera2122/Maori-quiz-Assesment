def question():
    i = 0
    while i < 2:
        answer = input("Question? (yes or no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            print("Yes")
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('Please enter yes or no')
            else:
                print("Nothing done")


question()

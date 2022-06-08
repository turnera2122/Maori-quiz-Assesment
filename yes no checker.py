def yesno(question):
    """Simple Yes/No Function."""
    prompt = f'{" Is toru the correct Maori word for 3?"} ? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print(f'{ans} is invalid, please try again...')
        return yesno(question)
    if ans == 'y':
        return True
    return False


def main():
    """Run main function."""
    ans = yesno("What'll it be")
    print(f'you answer was: {ans}')



if __name__ == '__main__':
    main()

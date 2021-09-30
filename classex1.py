lower_limit = int(input('Enter lower limit: '))
upper_limit = int(input('Enter upper limit: '))

def evnum():
    for evval in range(lower_limit, upper_limit):
        if evval % 2 == 0:
            print (evval)

def odnum():
    for oddval in range(lower_limit, upper_limit):
        if oddval % 2 == 1:
            print(oddval)

def evaluate():
    option = str(input('Select display even or odd numbers. Type E for even and O for odd: '))
    option = option.upper()
    if option == 'E':
        evnum()
    elif option == 'O':
        odnum()
    else :
        print('Invalid entry. Try again.')

evaluate()

option1 = 'Y' or 'N'
while option1 != 'Y' or 'N':
    option1 = str(input('Calculate new range of values? (Y/N): '))
    option1 = option1.upper()
    if option1 == 'Y':
        lower_limit = int(input('Enter new lower limit: '))
        upper_limit = int(input('Enter new upper limit: '))
        evaluate()
    elif option1 == 'N':
        print('Thank you for your input!')
        quit()
    else:
        print('Invalid entry. Try again.')
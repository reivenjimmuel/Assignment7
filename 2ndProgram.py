# A function in evaluating if the password has more than 15 characters
def countPassword(passwordF):
    nPasswordF = len(passwordF)
    if nPasswordF >= 16:
        nPasswordF = 'VALID'
        return nPasswordF
    else:
        nPasswordF = 'INVALID'
        return nPasswordF

# A function to count the number of capital letters, numbers, and special characters
def evaluateCharacters(passwordF):
    smallLetter = 0
    capitalLetter = 0
    number = 0
    spaces = 0
    specialCharacter = 0

    for c in passwordF:
        if c.islower():
            smallLetter = smallLetter + 1
        elif c.isupper():
            capitalLetter = capitalLetter +1
        elif c.isnumeric():
            number = number + 1
        elif c == ' ':
            spaces = spaces + 1
        else:
            specialCharacter = specialCharacter + 1
    return capitalLetter, number, specialCharacter

# A function in evaluating if the password has at least one (1) capital letter, number, and special character
def evaluatePassword(passwordF, passwordCountF, nCapLetterF, nNumberF, nSpecCharacF):
    if passwordCountF == 'VALID' and nCapLetterF >= 1 and nNumberF >= 1 and nSpecCharacF >=1:
        print(f'''
Input: {passwordF}
Output: VALID
	''')
    else:
        print(f'''
Input: {passwordF}
Output: INVALID
	''')

# Get user input
print('Is Your Password Valid?')
password = input('Enter your Password: ')

# A condition if the password has a space or not before proceeding
if ' ' in password:
    print('Error. Password must not have any spaces.')
else:
    passwordCount = countPassword(password)
    nCapLetter, nNumber, nSpecCharac = evaluateCharacters(password)
    evaluatePassword(password, passwordCount, nCapLetter, nNumber, nSpecCharac)
print('Welcome to Words, Vowels, and Consonants Counter!')

# Get user input and capitalized it. Also used strip function to count the number of words
userInput = input('Enter your sentence: ')
sentence = userInput.upper()
nSentence = sentence.strip()

# Value of vowels and consonants to be used in the for-loop function
vowels = ['A', 'E', 'I', 'O', 'U']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

# Counter for the nummber of needed variables
nWords = 1
nVowels = 0
nConsonants = 0

# For-loop function
for c in nSentence:
	if c == ' ':
		nWords = nWords + 1
	elif c in vowels:
		nVowels = nVowels + 1
	elif c in consonants:
		nConsonants = nConsonants + 1

# Display output
print(f'''
Input: {userInput}
Words: {nWords}
Vowels: {nVowels}
Consonants: {nConsonants}

Thank you for using Words, Vowels, and Consonants Counter!
	''')
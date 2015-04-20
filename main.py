vowels = 'AEIOUaeiou';
def PigWord(input):
	"Print input in pig latin"
	if input == "exit":
		return "Ankthay ouyay orfay usingway Igpay Atinlay Anslatortray!";
	elif input[0] in vowels:
		# if first letter is a vowel, just append a postfix
		return ''.join(input) + "way";
	else:
		# find out where the first vowel is indexed
		# then use that to slice the input into
		# a beginning and end. rearrange them and
		# append a postfix.
		index = firstVowel(input);
		engBegin = input[0:index];
		engEnd = input[index:];
		pigWord = engEnd + engBegin + "ay";
		return pigWord;
				
def firstVowel(input):
	"Returns index location of first vowel"
	i = 0;
	for char in input:
		if char not in vowels:
			i += 1;
		else:
			return i;
			break;
			
print "Welcome to the Igpay Atinlay Anslatortray";

# Allow user to translate until program is closed or exited
while input != "exit":
	input = raw_input("\nWhat would you like translated? ");
	inputList = input.split(); # in case the user inputs a sentence, split each word into a list
	
	# iterate through the list of words
	for words in inputList:
		# to prevent 'Latin' -> 'atinLay' the input should be lowercase.
		# then capitalize the output: 'Atinlay'
		# otherwise, just process the word as normal
		if words[0].isupper():
			print PigWord(words.lower()).title(),
		else:
			print PigWord(words),


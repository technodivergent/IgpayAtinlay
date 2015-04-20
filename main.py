vowels = 'aeiou';
def PigLatin(input):
	"Print input in pig latin"
	if input == "exit":
		return "Ankthay ouya orfay usingway Igpay Atinlay Anslatortray!";
	elif input[0] in vowels:
		return ''.join(input) + "way";
	else:
		index = firstVowel(input);
		engBegin = input[0:index];
		engEnd = input[index:];
		pigLatin = engEnd + engBegin + "ay";
		return pigLatin;
				
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
print ""

while input != "exit":
	input = raw_input("What would you like translated? ");
	print PigLatin(input);


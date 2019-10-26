import json

from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
	w=w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w,data.keys())) > 0:
		choice=input("Did You mean %s instead ? Enter Y if yes , or N if no :" % get_close_matches(w,data.keys())[0])
		if choice=="Y " or choice == "y":

			return data[get_close_matches(w,data.keys())[0]]

		elif choice =="N" or choice == "n":

			return "The Word doesn't find please double check it "

		else:
			return " We didn't Understand your entry. "


	else:
		return "The Word doesn't find please double check it "



word=input("Enter Word :")

output=translate(word)

if type(output) == list:
	for i in output:
		print(i)

else:
	print(output)
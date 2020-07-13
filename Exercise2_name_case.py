#create a Variable for a name and print a message to that person
name = "Hello Eric, would you like to learn some Python today?"
print(name)

#create a variable to represent a person then print the name in lower,upper and title case
name = "pratik"
print(name.upper())
print(name.lower())
print(name.title())

#write a quote from a famous person and print the quote and name of it author
person = "albert einstein"
quote = '"A person who never made a mistake never tried anything new."' 

message = f"{person.title()} once said, {quote.upper()}"
print(message)

#create a variable to represent a person's name and include some whitespace at the beginning and end of the name
#use character combination, "\t" and "\n" atleast once
person_name = " Pratik Rai "
print(person_name)
print(person_name.rstrip())
print(person_name.lstrip())
print(person_name.strip())

lesson = "I would like to learn: \t\nPython \t\nJava \t\nC# and \t\nJavaScript"
print(lesson)
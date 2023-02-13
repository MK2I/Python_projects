# So terminal outputs "Greetings: " then i used capitalize so the first letter is capital and rest lowercase

# removed all case distinctions with casefold although i could use just "lower()"

# lastly i used strip to remove spaces
user_input = input("Gretings: ").capitalize().casefold().strip()

# here i told the program to slice from 0 to 5 letters.
if user_input[0:5] == "hello":
    print("$0")

# if the greetings start with h but not hello (20$)
elif user_input[0] == "h":
    print("$20")
# otherwise output 100$
else:
    print("$100")


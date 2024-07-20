#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as test:
    invited_list = test.readlines()

with open("./Input/Letters/starting_letter.txt") as mail:
    mail_example = mail.readlines()
    mail_in_str = ("".join(str(x) for x in mail_example))

# Loop through invited_list and replace the name in the letter
for name in invited_list:
    new_name = name.strip("\n")
    print(new_name)
    with open("./Output/ReadyToSend/" + new_name + "_mail.txt", "w") as new_mail:
        content = mail_in_str.replace("[name]", new_name)
        new_mail.write(content)
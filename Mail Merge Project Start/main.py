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

with open("./Output/ReadyToSend/" + "hello22" + ".txt", "a") as new_mail:
    pass



# Loop through invited_list and replace the name in the letter
# for _ in invited_list:

    # with open("./Output/ReadyToSend/" + _ + "_mail.txt", "a") as new_mail:
    #     mail_in_str.replace("[name]", _)
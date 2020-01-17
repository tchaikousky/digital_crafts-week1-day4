# my_string = "atlanta falcons"
# print(my_string.upper()) #all caps
# print(my_string.title()) #first letter of each word

# count = len(my_string)
# new_string = ""
# while(count > 0):
#     new_string += my_string[count - 1]
#     count -= 1

# print(new_string)

# paragraph = input("Type a few sentences. ").upper()
# count = 0
# new_string = ""

# while(count < len(paragraph)):
#     if(paragraph[count] == "A"):
#         new_string += "4"
#     elif(paragraph[count] == "E"):
#         new_string += "3"

#     elif(paragraph[count] == "G"):
#         new_string += "6"

#     elif(paragraph[count] == "I"):
#         new_string += "1"

#     elif(paragraph[count] == "O"):
#         new_string += "0"

#     elif(paragraph[count] == "S"):
#         new_string += "5"

#     elif(paragraph[count] == "T"):
#         new_string += "7"
#     else:
#         new_string += paragraph[count]
    
#     count += 1
    
# print(new_string)    

word = input("Enter a word: ").lower()
count = 0
new_word = ""

while(count < len(word)):
    letter = word[count]
    new_word += letter
    
    if(count > 0):
        if(word[count] == word[count - 1]):
            if(letter == "a"):
                new_word += "aaa"
            elif(letter == "e"):
                new_word += "eee"
            elif(letter == "i"):
                new_word += "iii"
            elif(letter == "o"):
                new_word += "ooo"
            elif(letter == "u"):
                new_word += "uuu"
            else:
                new_word += letter
    count += 1

print(new_word)

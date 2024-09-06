
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    #Create an array from the text, split by whitespace
    txt = txt.split()
    #Create a variable to track if the last character is a letter
    lastCharIsLetter = False
    #Iterate over the array
    for i in txt:
        #Set the last character variable to the last character in the string
        lastChar = i[-1]
        #Check if the last character is in the alphabet
        if lastChar.isalpha():
            #If it is, set the variable to True
            lastCharIsLetter = True
    #Return the variable
    return lastCharIsLetter

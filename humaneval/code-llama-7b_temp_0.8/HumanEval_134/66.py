
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
    #Create a variable to store the last letter.
    last_letter=txt[-1]
    #Create a variable to store the whole word
    word=txt
    #Create a variable to check if the last letter of a word is a letter
    letter=False
    #Create a variable to check if the word is empty
    empty=False
    #Create a variable to store the index of the last letter in the word
    index_last_letter=len(word)-1
    #Create a variable to store the word before the last letter
    word_before_last_letter=word[:index_last_letter]
    #Create a variable to check if there are spaces in the word before the last letter
    spaces=False
    #Check if there are spaces in the word before the last letter
    if " " in word_before_last_letter:
        spaces=True
    #Check if the word is empty
    if len(txt)==0:
        empty=True
    #Check if the last letter of a word is a letter
    if (last_letter.isalpha()==True) and (spaces==True):
        letter=True
    #Return the value for the function
    return letter

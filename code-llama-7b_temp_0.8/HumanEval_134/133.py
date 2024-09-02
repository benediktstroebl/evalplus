
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
    #create a list of all the words in the string
    word_list = txt.split()
    #if the string is empty return false
    if len(txt) == 0:
        return False
    else:
        #find the last char of the last word in the list
        last_char = word_list[-1][-1]
        #convert last_char to an int, if it can be, then it is not a letter
        try:
            last_char_int = int(last_char)
        except ValueError:
            return False
        else:
            return True

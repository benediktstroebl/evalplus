
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

    txt = txt.split()
    if txt[-1] == '':
        return False
    else:
        if txt[-1][-1] == ' ':
            return False
        else:
            if txt[-1][-1] == 'a' or txt[-1][-1] == 'b' or txt[-1][-1] == 'c' or txt[-1][-1] == 'd' or txt[-1][-1] == 'e' or txt[-1][-1] == 'f' or txt[-1][-1] == 'g' or txt[-1][-1] == 'h' or txt[-1][-1] == 'i' or txt[-1][-1] == 'j' or txt[-1][-1] == 'k' or txt[-1][-1] == 'l' or txt[-1][-1] == 'm' or txt[-1][-1] == 'n' or txt[-1][-1] == 'o' or txt[-1][-1] == 'p' or txt[-1][-1] == 'q' or txt

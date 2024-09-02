
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
    #   [start_index, end_index]
    #   last_word_index = len(txt) - txt.rindex(" ")[::-1]
    #   last_index = len(txt) - 1
    #   last_char = txt[-1]
    #   word_after_last_index = txt[last_word_index+1:last_index]
    #   if word_after_last_index.isalpha() and last_char not in word_after_last_index:
    #       return True
    #   else:
    #       return False

    #   for i in range(len(txt)-1):
    #       if txt[i] not in " " and txt[i].isalpha() and txt[i+1] in " ":
    #           return True
    #       else:
    #           return False

    #   for i in range(len(txt) - 1, -1, -1):
    #       if txt[i].isalpha() and txt[i] not in " ":
    #           return True

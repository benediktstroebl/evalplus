
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

    if txt != '':
        if txt[-1].isalpha() and not txt[-1].isalnum():
            return False
        else:
            return True
    else:
        return False

    # The first line is the function name.
    # The second line is your code.
    # The third line is the return value or result of the function.
    # The fourth line is the parameter or argument of the function.
    # The fifth line and below are the test cases.
    # The test cases will be auto-evaluated and auto-grader will only
    # give feedback on your code but not the results.


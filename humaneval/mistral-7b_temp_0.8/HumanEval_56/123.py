

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    opening_brackets = '><'
    closing_brackets = '<>'
    opening_brackets_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    closing_brackets_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    # compare each character in brackets to opening_brackets.
    # if they are the same, return false
    for character in brackets:
        if character in opening_brackets:
            return False

    # compare each character in brackets to closing_brackets.
    # if they are the same, return false
    for character in brackets:
        if character in closing_brackets:
            return False

    # compare each character in brackets to opening_brackets_dict.
    # if they don't match and the key is in brackets, return false.
    for character in brackets:
        if character in opening_brackets_

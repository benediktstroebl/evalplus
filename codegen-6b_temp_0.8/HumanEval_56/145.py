

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
    "*** YOUR CODE HERE ***"
    dictionary = {'<':'>','>':'<','[':']','{':'}','(':')'}

    list = list(brackets)
    for index in range(len(list)):
        if list[index] in dictionary and list[index] != dictionary[list[index]]:
            return False

    return True

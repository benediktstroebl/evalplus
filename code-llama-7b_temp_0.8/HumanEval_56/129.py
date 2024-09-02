

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
    # count the number of opening brackets
    # and the number of closing brackets
    count_open = count_close = 0
    for letter in brackets:
        if letter == '<':
            count_open += 1
        elif letter == '>':
            count_close += 1

    # if the number of opening brackets is not
    # equal to the number of closing brackets,
    # then the bracketing is incorrect
    return count_open == count_close


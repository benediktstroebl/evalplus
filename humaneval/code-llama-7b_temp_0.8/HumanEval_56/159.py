

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

    # PAST YOUR CODE HERE
    if len(brackets) == 0:
        return True
    elif len(brackets) == 1:
        return False

    if brackets[0] == '<':
        if brackets[1] == '>':
            return correct_bracketing(brackets[2:])
        else:
            return False
    else:
        return correct_bracketing(brackets[1:])


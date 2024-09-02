

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

    # count how many opening brackets are there
    open = 0
    for bracket in brackets:
        if bracket == "<":
            open += 1
        else:
            open -= 1

    # if number of opening brackets and closing brackets is not the same,
    # then they are not correctly bracketed.
    if open != 0:
        return False
    else:
        return True


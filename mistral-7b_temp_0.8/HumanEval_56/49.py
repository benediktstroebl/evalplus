

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
    opening_brackets = "<>"
    count = 0
    for i in brackets:
        if i in opening_brackets:
            count += 1
        else:
            count -= 1
    if count == 0:
        return True
    else:
        return False

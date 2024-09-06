

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
    for i, bracket in enumerate(brackets):
        if bracket!= "<" and bracket!= ">":
            return False
        if (i + 1) < len(brackets) and not brackets[i + 1].isalnum():
            return False
    return True


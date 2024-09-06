

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
    # check that every opening bracket has a corresponding closing bracket
    for bracket in brackets:
        if bracket == "<":
            if not bracket.replace(">", "") in brackets:
                return False
        elif bracket == ">":
            if not bracket.replace("<", "") in brackets:
                return False
    return True
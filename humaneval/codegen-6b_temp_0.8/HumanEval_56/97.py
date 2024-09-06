

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
    n = 0
    for bracket in brackets:
        if n % 2 == 0:
            if bracket != ">":
                return False
        else:
            if bracket != "<":
                return False
        n += 1

    return True

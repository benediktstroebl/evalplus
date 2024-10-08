

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
    for i in range(len(brackets) - 1):
        if bracket =="<":
            if not brackets[i+1] == ">":
                return False
        elif bracket == ">":
            if not brackets[i] == "<":
                return False
        else:
            if not brackets[i] == brackets[i+1]:
                return False
    return True


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
    i = 0
    while len(brackets) > i:
        if brackets[i] == ">":
            if i == 0 or brackets[i-1] != "<":
                return False
            else:
                i += 1
        else:
            i += 1
    return True
    

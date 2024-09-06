

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
    s = 0
    for c in brackets:
        if c == ">":
            if s == 0:
                return False
            s -= 1
        if c == "<":
            s += 1
    if s!= 0:
        return False
    return True

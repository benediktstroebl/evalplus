

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
    s = []
    for b in brackets:
        if b == "<":
            s.append("<")
        else:
            if s and s[-1] == "<":
                s.pop()
            else:
                return False
    if s:
        return False
    return True

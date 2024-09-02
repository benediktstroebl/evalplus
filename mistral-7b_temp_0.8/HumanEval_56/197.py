

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
    l = len(brackets)
    if l % 2 != 0:
        return False
    opened = 0
    for x in brackets:
        if x == "<":
            opened += 1
        elif x == ">":
            opened -= 1
        if opened < 0:
            return False
    return True


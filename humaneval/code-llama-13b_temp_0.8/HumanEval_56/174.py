

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
    opened = 0
    for ch in brackets:
        if ch == '<':
            opened += 1
        elif ch == '>':
            if opened == 0:
                return False
            else:
                opened -= 1
    return opened == 0

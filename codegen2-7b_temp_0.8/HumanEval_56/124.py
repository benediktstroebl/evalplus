

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
    brackets = set(brackets)
    openers = set("<>")
    for i, c in enumerate(brackets):
        if c not in openers:
            return False
        if c in openers:
            openers.remove(c)
    return len(openers) == 0

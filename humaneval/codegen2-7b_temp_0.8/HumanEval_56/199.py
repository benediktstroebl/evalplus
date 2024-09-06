

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
    unbalanced = []
    for i, c in enumerate(brackets):
        if c == ">":
            unbalanced.append(c)
        else:
            unbalanced.pop()
            if not unbalanced:
                return True
    return False


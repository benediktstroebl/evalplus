

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
    idx = 0
    while idx < len(brackets):
        if brackets[idx] == ">":
            idx += 1
            if brackets[idx] == "<":
                return False
        idx += 1
    return True



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
    opening_brackets = "><"
    for i in range(len(brackets) - 1):
        if brackets[i] not in opening_brackets:
            return False
        if brackets[i+1] not in opening_brackets:
            return False
    return True


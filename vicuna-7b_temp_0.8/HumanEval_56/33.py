

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
        if bracket =="" or bracket[0] != brackets[i]:
            return False
        if i + 1 < len(brackets) and brackets[i] != brackets[i + 1]:
            return False
    return True

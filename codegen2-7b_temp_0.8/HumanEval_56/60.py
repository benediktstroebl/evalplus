

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
    while i < len(brackets) - 1:
        if brackets[i] == "<" and brackets[i+1] == ">":
            i += 2
        else:
            return False
        i += 1
    return True

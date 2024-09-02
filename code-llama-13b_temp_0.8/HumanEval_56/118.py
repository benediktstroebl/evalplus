

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

    if len(brackets) % 2 == 0:
        return True

    if len(brackets) == 1:
        return False

    stack = 0
    for bracket in brackets:
        if bracket == "<":
            stack += 1
        else:
            if stack == 0:
                return False
            stack -= 1

    if stack != 0:
        return False

    return True



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
    result = 0
    for item in brackets:
        if item == "<":
            result += 1
        if item == ">":
            result -= 1
        if result < 0:
            return False
    return result == 0


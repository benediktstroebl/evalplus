

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
    open = 0
    for bracket in brackets:
        if bracket == ">":
            if open == 0:
                return False
            open -= 1
        if bracket == "<":
            open += 1
    return open == 0

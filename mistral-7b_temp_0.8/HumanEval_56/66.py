

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
    if len(brackets) % 2 != 0:
        return False

    closed = []
    for bracket in brackets:
        if bracket == "<":
            closed.append("<")
        else:
            if len(closed) == 0 or closed.pop() != ">":
                return False

    if len(closed) != 0:
        return False

    return True

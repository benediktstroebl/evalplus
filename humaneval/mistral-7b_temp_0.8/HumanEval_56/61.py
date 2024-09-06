

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
    num_open, num_closed = 0, 0
    for bracket in brackets:
        if bracket == "<":
            num_open += 1
        elif bracket == ">":
            num_closed += 1
        else:
            return False
    return num_open == num_closed


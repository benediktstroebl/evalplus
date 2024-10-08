

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
    num_open = 0
    for bracket in brackets:
        if bracket == "<":
            num_open += 1
        elif bracket == ">":
            if num_open == 0:
                return False
            else:
                num_open -= 1
    if num_open == 0:
        return True
    else:
        return False

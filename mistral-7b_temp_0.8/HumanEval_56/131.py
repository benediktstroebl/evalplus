

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
    n_left_bracket = 0
    for c in brackets:
        if c == "<":
            n_left_bracket += 1
        else:
            n_left_bracket -= 1
    return n_left_bracket == 0

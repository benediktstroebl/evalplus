

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
    # return (open_brackets := reduce(lambda x, y: (x - 1, y) if y == '>' else (x + 1, y), list(brackets), (0, None))[0]) == 0
    return reduce(lambda x, y: x - 1 if y == '>' else x + 1, list(brackets), 0) == 0

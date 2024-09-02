

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
    n = len(brackets)
    pair = []
    for marker, open, close in brackets_iterator(brackets):
        pair.append(close)
        if len(pair) > 2:
            return False
    return len(pair) == 2 * n

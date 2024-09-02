

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
    n = 0
    for c in brackets:
        if c == ">":
            n += 1
        elif c == "<":
            n -= 1
        if n < 0:
            return False
    return n == 0

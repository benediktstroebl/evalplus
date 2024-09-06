

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

    unmatched = 0
    for b in brackets:
        if b == "<":
            unmatched += 1
        else:
            unmatched -= 1
        if unmatched < 0:
            return False
    return unmatched == 0


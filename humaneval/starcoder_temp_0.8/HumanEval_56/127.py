

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
    # initialize counter
    count = 0

    # loop through string
    for b in brackets:
        if b == "<":
            count += 1
        if b == ">":
            count -= 1

    # if count is zero, then all brackets are well-formed.
    return count == 0

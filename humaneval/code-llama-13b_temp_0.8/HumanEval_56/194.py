

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

    # Your code here
    if not brackets:
        return True
    i = 0
    for ch in brackets:
        if ch == "<":
            i += 1
        else:
            i -= 1
        if i < 0:
            return False
    if i == 0:
        return True
    return False


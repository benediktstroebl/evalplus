

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
    opening = []
    for b in brackets:
        if b == "<":
            if len(opening) == 0:
                return False
            opening.pop()
        else:
            opening.append(b)
    if len(opening)!= 0:
        return False
    return True

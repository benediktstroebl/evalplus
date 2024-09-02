

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
    for c in brackets:
        if c == "<":
            opening.append(c)
        elif c == ">":
            if opening:
                opening.pop()
            else:
                return False
    return not opening

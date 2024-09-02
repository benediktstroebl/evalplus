

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
    if len(brackets) % 2 != 0:
        return False
    opening = "><"
    closing = "<>"
    for bracket in brackets:
        if bracket == "<" or bracket == ">":
            if len(opening) == 0 or len(closing) == 0:
                return False
            opening = opening[1:]
            closing = closing[1:]
        elif bracket == ">" and len(closing) == 0:
            return False
        elif bracket == "<" and len(opening) == 0:
            return False
        else:
            return False
    return True

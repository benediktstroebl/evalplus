

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
    opening_brackets = 0
    for c in brackets:
        if c == "<":
            opening_brackets += 1
        else:
            if opening_brackets == 0:
                return False
            opening_brackets -= 1
    return opening_brackets == 0

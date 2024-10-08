

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
    for bracket in brackets:
        if bracket == "<":
            opening_brackets += 1
        elif bracket == ">":
            if opening_brackets == 0:
                return False
            else:
                opening_brackets -= 1
    return opening_brackets == 0


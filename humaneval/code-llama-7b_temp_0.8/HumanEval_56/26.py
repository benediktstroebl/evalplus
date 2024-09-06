

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
    opened_brackets = 0

    for bracket in brackets:
        if bracket == "<":
            opened_brackets += 1
        elif bracket == ">":
            opened_brackets -= 1

        if opened_brackets < 0:
            return False

    return opened_brackets == 0


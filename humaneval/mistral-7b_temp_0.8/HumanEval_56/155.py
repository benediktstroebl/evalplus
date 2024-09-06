

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
    openings = 0
    closings = 0
    for bracket in brackets:
        if bracket == "<":
            openings += 1
        elif bracket == ">":
            closings += 1
        if openings < closings:
            return False
    return openings == closings


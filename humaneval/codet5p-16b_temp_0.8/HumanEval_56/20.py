

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

    openings = []
    for bracket in brackets:
        if bracket == "<":
            openings.append(bracket)
        elif bracket == ">":
            if not openings:
                return False
            openings.pop()
    return not openings

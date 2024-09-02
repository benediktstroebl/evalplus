

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
    for b in brackets:
        if b == "<":
            openings.append(b)
        else:
            if not openings:
                return False
            else:
                openings.pop()

    return len(openings) == 0







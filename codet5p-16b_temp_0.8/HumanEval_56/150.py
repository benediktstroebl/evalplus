

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

    openings = set()
    for bracket in brackets:
        if bracket == '<':
            openings.add(bracket)
        elif bracket == '>':
            if openings:
                openings.pop()
            else:
                return False
    return len(openings) == 0


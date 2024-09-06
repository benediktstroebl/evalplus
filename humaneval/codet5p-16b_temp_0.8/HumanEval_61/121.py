

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    openings = []
    closings = []
    for bracket in brackets:
        if bracket == "(":
            openings.append(bracket)
        else:
            if len(openings) == 0:
                return False
            else:
                closings.append(bracket)
                openings.pop()
    if len(openings)!= 0:
        return False
    return True


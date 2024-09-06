

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
    opend = 0
    closed = 0
    for b in brackets:
        if b == "(":
            opend += 1
        elif b == ")":
            closed += 1
    return closed == opend

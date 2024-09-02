

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
    for i, b in enumerate(brackets):
        if b == "(":
            openings.append(i)
        elif b == ")":
            if openings:
                openings.pop()
            else:
                return False
    if not openings:
        return True
    return False


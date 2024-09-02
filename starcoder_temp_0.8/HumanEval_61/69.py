

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
    lefts = 0
    rights = 0
    for s in brackets:
        if s == '(':
            lefts += 1
        else:
            rights += 1

        if lefts < rights:
            return False
    return lefts == rights

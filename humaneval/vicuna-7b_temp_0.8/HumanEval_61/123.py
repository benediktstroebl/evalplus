

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
    for opening, closing in zip(brackets.strip('()'), brackets.strip('(')):
        if not closing or not opening:
            return False
        elif opening == closing:
            return True
    return False

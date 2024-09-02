

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
    if len(brackets) % 2 != 0:
        return False
    for opening_brace in brackets:
        for i in range(1, len(opening_brace)):
            if not bracket_corresponds(opening_brace[:i], opening_brace[i+1:]):
                return False
    return True

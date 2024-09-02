

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
    if not brackets:
        return True

    for opening_brace in brackets:
        for i in range(1, len(opening_brace)):
            if not brackets[i-1] == opening_brace[0] and brackets[i] != opening_brace[1]:
                return False

    return True



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
    for open_brace in brackets:
        for i in range(1, len(open_brace)):
            if not brackets[i-1] == open_brace[0]:
                return False
        if brackets[len(open_brace)-1] != open_brace[1]:
            return False
    return True
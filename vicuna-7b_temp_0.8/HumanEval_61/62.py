

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
            if bracket_is_opening(open_brace[:i+1]) and bracket_is_closing(open_brace[i:i+2]):
                return True
    return False

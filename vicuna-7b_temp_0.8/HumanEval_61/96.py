

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
    for opening_brace in brackets:
        for i in range(1, len(opening_brace)):
            if opening_brace[i] != '(':
                return False
        for closing_brace in brackets[1:]:
            if closing_brace != opening_brace[0]:
                return False
    return True

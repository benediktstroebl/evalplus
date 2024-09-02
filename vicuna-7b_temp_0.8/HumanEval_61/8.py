

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
        if not brackets:
            return False
        for i in range(len(opening_brace)):
            if brackets[i+1] != opening_brace[::-1]:
                return False
        if brackets[len(opening_brace)-1] != ")"[::-1]:
            return False
    return True



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
    opening_brackets = "({["
    returning = True
    for bracket in brackets:
        if bracket in opening_brackets:
            if returning:
                returning = False
                continue
            else:
                return False
        elif not returning:
            returning = True
    return returning

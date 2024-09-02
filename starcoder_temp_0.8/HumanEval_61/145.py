

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
    lst = []
    for b in brackets:
        if b == "(":
            lst.append(b)
        else:
            if not lst:
                return False
            lst.pop()
    if not lst:
        return True
    return False

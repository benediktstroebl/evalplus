

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
    l = []
    for b in brackets:
        if b == "(":
            l.append(b)
        elif b == ")":
            if len(l) == 0:
                return False
            else:
                l.pop()
    if len(l) == 0:
        return True
    else:
        return False



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
    start = 0
    d = {}
    for i in range(len(brackets)):
        if brackets[i] == "(":
            d[brackets[i]] = i
        elif brackets[i] == ")":
            if d[brackets[i-1]] is not None:
                start = max(start, d[brackets[i-1]] + 1)
        else:
            return False
    else:
        return False
    for i in range(len(brackets)):
        if (i < start or i > start + 1) and d[brackets[i]] is not None:
            return False
    else:
        return True
        

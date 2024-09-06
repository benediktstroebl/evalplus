

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
    i = 0
    while i < len(brackets):
        if brackets[i] == "(":
            if i + 1 < len(brackets):
                if brackets[i + 1] == ")":
                    return False
            i += 1
        if brackets[i] == ")":
            if i + 1 < len(brackets):
                if brackets[i + 1] == "(":
                    return False
            i += 1
    return True




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
    if len(brackets) == 0 or len(brackets) % 2 != 0:
        return False
    idx = 0
    while idx < len(brackets):
        if brackets[idx] == "(":
            if idx + 1 < len(brackets) and brackets[idx+1] == ")":
                idx += 2
            else:
                return False
        else:
            return False
        idx += 1
    return True



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
    n = len(brackets)
    if n % 2!= 0:
        return False
    for i in range(0, n, 2):
        if brackets[i]!= ")":
            return False
    return True

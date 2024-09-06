

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
    if not brackets:
        return True
    l = len(brackets)
    balanced = 0
    i = 0
    while i < l:
        balanced += 1
        if balanced == 0:
            return False
        if brackets[i] == "(":
            balanced -= 1
        if balanced == 0:
            return False
        if brackets[i] == ")":
            balanced += 1
        i += 1
    return balanced == 0




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
    if len(brackets) == 0:
        return True
    for i in range(1, len(brackets)):
        if not is_match(brackets[i-1], brackets[i], brackets[i-1] != brackets[i]):
            return False
    return True

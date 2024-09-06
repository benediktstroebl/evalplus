

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
        return False
    for b in brackets:
        if b != brackets[0] and b != brackets[-1]:
            return False
        if b == brackets[0]:
            for i in range(1, len(brackets)):
                if brackets[i] != brackets[i-1]:
                    return False
        else:
            for i in range(1, len(brackets)):
                if brackets[i] != brackets[i-1] or brackets[i] != brackets[i+1]:
                    return False
    return True

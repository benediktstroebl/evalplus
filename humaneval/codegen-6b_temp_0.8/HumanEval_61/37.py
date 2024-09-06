

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
    if brackets[0] == ")" or brackets[0] == ")":
        return False
    if brackets[-1] == "(":
        return False
    count = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            count += 1
        elif brackets[i] == ")":
            count -= 1
        if count < 0:
            return False
    return True



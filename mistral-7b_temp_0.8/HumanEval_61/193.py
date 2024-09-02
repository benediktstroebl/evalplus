

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
    count = 0
    if brackets[0] == "(":
        count += 1
    if brackets[-1] == ")":
        count -= 1
    for b in brackets[1:-1]:
        if b == "(":
            count += 1
        if b == ")":
            count -= 1
    return count == 0


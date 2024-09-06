

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
    a = 0
    b = 0
    for c in brackets:
        if c == "(":
            a += 1
        elif c == ")":
            b += 1
        if a > b:
            return False
    return a == b


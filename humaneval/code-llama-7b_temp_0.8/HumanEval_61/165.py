

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

    bal = 0
    for c in brackets:
        if c == "(":
            bal += 1
        elif c == ")":
            bal -= 1
        else:
            continue
        if bal < 0:
            return False
    return bal == 0


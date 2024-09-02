

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
    depth = 0
    for bracket in brackets:
        if bracket == '(':
            depth += 1
        else:
            if depth == 0:
                return False
            depth -= 1
    return depth == 0


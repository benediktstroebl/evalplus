

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
    for i in brackets:
        if i == "(":
            depth += 1
        elif i == ")":
            if depth == 0:
                return False
            else:
                depth -= 1
    return depth == 0


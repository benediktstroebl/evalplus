

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
    for outer in brackets:
        if outer == "(":
            count += 1
        elif outer == ")":
            if count == 0:
                return False
            count -= 1
    return count == 0
    


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
    if brackets == "":
        return True
    if brackets[0] == ")":
        return False
    if brackets[-1] == "(":
        return False

    if correct_bracketing(brackets[1:-1]) == True:
        return True
    else:
        return False


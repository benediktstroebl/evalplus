

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
    if len(brackets) < 2:
        return True

    if brackets[0] == ")" and brackets[1] == "(":
        return False
    elif brackets[-1] == "(" and brackets[-2] == ")":
        return False
    else:
        return correct_bracketing(brackets[1:-1])


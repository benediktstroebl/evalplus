

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

    if brackets[0] == "(":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == ")":
        return False
    else:
        return correct_bracketing(brackets[1:]) and correct_bracketing(brackets[1:])


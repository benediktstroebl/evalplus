

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
    if len(brackets) == 1:
        return False
    elif len(brackets) == 2:
        return brackets == "()"
    elif brackets[0] == "(":
        if len(brackets) % 2 == 0:
            return correct_bracketing(brackets[1:-1])
        else:
            return correct_bracketing(brackets[1:])
    else:
        return correct_bracketing(brackets[1:])






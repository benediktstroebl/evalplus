

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
    if len(brackets) == 0:
        return True
    elif len(brackets) % 2 != 0:
        return False
    else:
        opening = brackets[0]
        if opening == ")":
            return False
        elif opening == "(":
            return correct_bracketing(brackets[1:])
        else:
            return correct_bracketing(brackets[2:])


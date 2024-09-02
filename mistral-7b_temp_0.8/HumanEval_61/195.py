

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
    elif len(brackets) % 2 == 1:
        return False
    else:
        first_bracket = brackets[0]
        if first_bracket == "(":
            return correct_bracketing(brackets[1:])
        elif first_bracket == ")":
            return False


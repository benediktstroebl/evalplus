

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
    if len(brackets) % 2 != 0:
        return False
    closing_bracket = brackets[len(brackets)-1]
    opening_bracket = brackets[0]
    if closing_bracket == "(":
        return False
    elif closing_bracket == ")":
        return True
    else:
        return False

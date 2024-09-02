

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
    if len(brackets) % 2 != 0:
        return False

    opening_brackets = 0
    for bracket in brackets:
        if bracket == "(":
            opening_brackets += 1
        elif bracket == ")":
            opening_brackets -= 1
        if opening_brackets < 0:
            return False

    if opening_brackets == 0:
        return True
    else:
        return False

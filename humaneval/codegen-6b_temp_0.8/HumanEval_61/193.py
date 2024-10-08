

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
    new = []
    for i, bracket in enumerate(brackets):
        if i < len(brackets) - 1:
            if bracket == "(" and brackets[i + 1] == ")":
                new.append("(")
    if len(new) == len(brackets):
        return True
    else:
        return False

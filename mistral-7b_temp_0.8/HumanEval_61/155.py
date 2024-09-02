

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

    assert type(brackets) == str
    if brackets == "":
        return True

    opened = 0
    for bracket in brackets:
        if bracket == "(":
            opened += 1
        elif bracket == ")":
            opened -= 1
        if opened < 0:
            return False
    return opened == 0


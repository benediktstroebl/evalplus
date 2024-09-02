

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

    count_opened = 0
    for b in brackets:
        if b == "(":
            count_opened += 1
        elif b == ")":
            if count_opened == 0:
                return False
            count_opened -= 1
    if count_opened != 0:
        return False
    return True

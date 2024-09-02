

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
    # count the number of opening and closing brackets
    num_open = 0
    num_close = 0
    for b in brackets:
        if b == "(":
            num_open += 1
        elif b == ")":
            num_close += 1
    if num_open != num_close:
        return False
    return True



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
    # count opening and closing brackets
    n_open, n_close = 0, 0
    for char in brackets:
        if char == "(":
            n_open += 1
        elif char == ")":
            n_close += 1
    return n_open == n_close

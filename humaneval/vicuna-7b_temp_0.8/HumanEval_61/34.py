

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
    # check if every opening bracket has a corresponding closing bracket
    for open_idx, close_idx in enumerate(brackets.split('(')):
        if open_idx != close_idx:
            return False
    return True
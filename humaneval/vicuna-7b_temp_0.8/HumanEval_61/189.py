

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
    # NOTE: This function is not the most efficient way to solve this problem.
    # For example, a stack or queue data structure could be used to keep track
    # of the open and closed brackets.
    for bracket in brackets:
        if bracket == "(":
            if not bracket in brackets:
                return False
        else:
            if not bracket in brackets:
                return False
    return True

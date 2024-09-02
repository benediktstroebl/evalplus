

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
    open_count, closed_count = 0, 0
    for b in brackets:
        if b == "(":
            open_count += 1
        else:
            closed_count += 1
        if open_count < closed_count:
            return False
    return open_count == closed_count

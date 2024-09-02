

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

    left_count = 0
    right_count = 0
    for bracket in brackets:
        if bracket == "(":
            left_count += 1
        elif bracket == ")":
            right_count += 1
        if right_count > left_count:
            return False
    if left_count > right_count:
        return False
    return True


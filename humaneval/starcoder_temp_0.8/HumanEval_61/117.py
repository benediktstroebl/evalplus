

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
    count_open = 0
    for bracket in brackets:
        if bracket == "(":
            count_open += 1
        else:
            count_open -= 1
        if count_open < 0:
            return False
    return count_open == 0


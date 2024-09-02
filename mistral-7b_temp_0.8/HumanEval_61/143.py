

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
    current_depth = 0
    for bracket in brackets:
        if bracket == "(":
            current_depth += 1
        else:
            current_depth -= 1
        if current_depth < 0:
            return False
    return current_depth == 0

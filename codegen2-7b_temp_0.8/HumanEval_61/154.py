

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
    if not brackets:
        return True
    if not brackets[0] == "(" or not brackets[-1] == ")":
        return False
    left_brackets = 0
    right_brackets = 0
    for c in brackets:
        if c == "(":
            left_brackets += 1
        elif c == ")":
            right_brackets += 1
    return left_brackets == right_brackets

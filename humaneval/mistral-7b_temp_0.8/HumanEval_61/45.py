

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

    # error: left_brackets is not defined
    left_brackets = 0

    # error: right_brackets is not defined
    right_brackets = 0

    for char in brackets:
        if char == "(":
            left_brackets += 1
        if char == ")":
            right_brackets += 1

    return left_brackets == right_brackets


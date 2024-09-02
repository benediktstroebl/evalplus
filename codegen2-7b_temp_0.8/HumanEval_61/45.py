

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
    left_bracket_count = right_bracket_count = 0
    for i in brackets:
        if i == "(":
            left_bracket_count += 1
        if i == ")":
            right_bracket_count += 1
            if left_bracket_count == 0:
                return False
            left_bracket_count -= 1

    return right_bracket_count ==

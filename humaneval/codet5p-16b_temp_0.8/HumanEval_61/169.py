

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

    brackets_list = list(brackets)
    bracket_count = 0
    for bracket in brackets_list:
        if bracket == "(":
            bracket_count += 1
        else:
            bracket_count -= 1
            if bracket_count < 0:
                return False

    return bracket_count == 0


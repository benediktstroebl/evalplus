

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
    opening_brackets_count = 0
    for bracket in brackets:
        if bracket == "(":
            opening_brackets_count += 1
        elif bracket == ")":
            opening_brackets_count -= 1

    return opening_brackets_count == 0


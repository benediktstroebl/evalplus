

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
    opening_bracket = 0
    closing_bracket = 0
    for bracket in brackets:
        if bracket == "(":
            opening_bracket += 1
        else:
            closing_bracket += 1

    return opening_bracket == closing_bracket


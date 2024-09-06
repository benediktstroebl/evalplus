

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
    opening_brackets = "("
    closing_brackets = ")"

    if len(brackets) % 2 != 0:
        return False

    opening_count = 0
    closing_count = 0
    for bracket in brackets:
        if bracket in opening_brackets:
            opening_count += 1
        elif bracket in closing_brackets:
            closing_count += 1

    if opening_count == closing_count:
        return True
    else:
        return False


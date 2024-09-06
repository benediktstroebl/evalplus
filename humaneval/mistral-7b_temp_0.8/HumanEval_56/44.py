

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    """
    if len(brackets) < 2:
        return False
    """
    opening_bracket_count = 0
    closing_bracket_count = 0
    for bracket in brackets:
        if bracket == "<":
            opening_bracket_count += 1
        elif bracket == ">":
            closing_bracket_count += 1
        if closing_bracket_count > opening_bracket_count:
            return False
    if closing_bracket_count == opening_bracket_count:
        return True
    return False


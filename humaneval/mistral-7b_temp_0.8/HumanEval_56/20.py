

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
    left_brackets = 0
    right_brackets = 0
    for i in brackets:
        if i == "<":
            left_brackets += 1
        if i == ">":
            right_brackets += 1
        if left_brackets > right_brackets:
            return False
        if left_brackets == 0 and right_brackets > 0:
            return False
    if left_brackets == right_brackets:
        return True
    return False

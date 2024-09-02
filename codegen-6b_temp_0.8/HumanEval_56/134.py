

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
    bracket_num = 0
    for bracket in brackets:
        if bracket == '<':
            bracket_num += 1
        elif bracket == '>':
            bracket_num -= 1
        if bracket_num < 0:
            return False
    return bracket_num == 0

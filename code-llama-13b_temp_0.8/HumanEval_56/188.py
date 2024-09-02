

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
    bracket_count = 0
    for b in brackets:
        if b == "<":
            bracket_count += 1
        else:
            bracket_count -= 1
        if bracket_count < 0:
            return False
    return bracket_count == 0




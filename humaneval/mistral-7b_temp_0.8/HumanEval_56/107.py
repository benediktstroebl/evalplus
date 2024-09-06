

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
    bracket_counter = 0
    for bracket in brackets:
        if bracket == "<":
            bracket_counter += 1
        elif bracket == ">":
            if bracket_counter == 0:
                return False
            else:
                bracket_counter -= 1
    return bracket_counter == 0




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
    # Check the first and last bracket
    if brackets[0] != brackets[-1]:
        return False

    # Check the rest of the brackets
    for i, bracket in enumerate(brackets[1:-1]):
        if bracket != brackets[i+1]:
            return False

    return True

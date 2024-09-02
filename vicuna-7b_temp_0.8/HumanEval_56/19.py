

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
    # Check for an empty string or a single brackets
    if not brackets:
        return True

    # Otherwise, check if every opening bracket is matched by a closing bracket
    for bracket in brackets:
        if bracket not in brackets:
            return False
    return True

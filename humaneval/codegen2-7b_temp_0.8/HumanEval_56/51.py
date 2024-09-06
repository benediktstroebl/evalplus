

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
    for opening_bracket, closing_bracket in brackets_to_brackets_map.items():
        if not any(bracket == opening_bracket for bracket in brackets):
            return False
        if not any(bracket == closing_bracket for bracket in brackets):
            return False
    return True




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
    bracket_counter = {}
    for bracket in brackets:
        if bracket == ">":
            bracket_counter["<"] = bracket_counter.get("<", 0) + 1
        else:
            bracket_counter["<"] = bracket_counter.get("<", 0) - 1
    return bracket_counter["<"] == 0




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

    # This counts the number of opening brackets ("<") in the string.
    # It is equivalent to len([ch for ch in brackets if ch == "<"])
    total_open = 0
    for ch in brackets:
        if ch == "<":
            total_open += 1

    # This counts the number of closing brackets (">") in the string.
    total_closed = 0
    for ch in brackets:
        if ch == ">":
            total_closed += 1

    return total_closed == total_open




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

    if len(brackets) % 2 != 0:
        return False
    opening_count = 0
    closing_count = 0
    for char in brackets:
        if char == "<":
            opening_count += 1
        else:
            closing_count += 1
        if opening_count < closing_count:
            return False
    return True


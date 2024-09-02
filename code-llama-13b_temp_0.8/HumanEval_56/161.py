

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

    count_open = 0
    count_close = 0

    for char in brackets:
        if char == "<":
            count_open += 1
        elif char == ">":
            count_close += 1

    if count_open == count_close:
        return True
    else:
        return False




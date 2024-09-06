

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

    count_left = 0

    for bracket in brackets:
        if bracket == "<":
            count_left += 1
        elif bracket == ">":
            if count_left == 0:
                return False
            count_left -= 1

    if count_left != 0:
        return False

    return True


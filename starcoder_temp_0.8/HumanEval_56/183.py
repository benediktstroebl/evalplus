

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

    count_brackets = 0
    for bracket in brackets:
        if bracket == ">":
            count_brackets -= 1
        elif bracket == "<":
            count_brackets += 1
        if count_brackets < 0:
            return False
    return count_brackets == 0




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

    bracket_list = list(brackets)
    brackets_count = 0

    for bracket in bracket_list:
        if bracket == "<":
            brackets_count += 1
        if bracket == ">":
            brackets_count -= 1
        if brackets_count < 0:
            return False

    return brackets_count == 0




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
    if not brackets:
        return True
    if len(brackets) == 1:
        return False
    if brackets[0] == ">" or brackets[-1] == "<":
        return False
    open_brackets = 0
    for bracket in brackets:
        if bracket == "<":
            open_brackets += 1
        if bracket == ">":
            if open_brackets == 0:
                return False
            open_brackets -= 1
    if open_brackets == 0:
        return True
    return False

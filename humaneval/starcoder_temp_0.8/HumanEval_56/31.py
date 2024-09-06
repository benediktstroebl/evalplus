

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
    open_brackets = 0
    for i in brackets:
        if i == "<":
            open_brackets += 1
        elif i == ">":
            open_brackets -= 1
    if open_brackets == 0:
        return True
    else:
        return False

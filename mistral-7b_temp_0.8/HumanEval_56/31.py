

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
    if len(brackets) == 0:
        return True

    if brackets[0] == "<":
        open_brackets = 1
    else:
        open_brackets = -1

    for c in brackets:
        if c == "<":
            open_brackets += 1
        elif c == ">":
            open_brackets -= 1

        if open_brackets < 0:
            return False

    return open_brackets == 0





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

    opening = "<"
    closing = ">"

    for bracket in brackets:
        if bracket == opening:
            open_brackets += 1
        else:
            close_brackets += 1

    if open_brackets == close_brackets:
        return True
    else:
        return False


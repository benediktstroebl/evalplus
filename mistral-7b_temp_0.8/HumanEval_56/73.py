

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

    num_opening = 0
    num_closing = 0

    for c in brackets:
        if c == "<":
            num_opening += 1
        elif c == ">":
            num_closing += 1

    if num_opening == num_closing:
        return True
    else:
        return False




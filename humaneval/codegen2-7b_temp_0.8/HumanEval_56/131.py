

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
    for i, c in enumerate(brackets):
        if c == '<':
            open_brackets += 1
        elif c == '>':
            if open_brackets == 0:
                return False
            open_brackets -= 1
    return open_brackets ==

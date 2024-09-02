

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
    # count how many opening and closing brackets there are
    open_brackets = 0
    for b in brackets:
        if b == '<':
            open_brackets += 1
        if b == '>':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                return False
    return open_brackets == 0

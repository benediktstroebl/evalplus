

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

    opened = 0
    for i in brackets:
        if i == '<':
            opened += 1
        elif i == '>':
            opened -= 1
        if opened < 0:
            return False
    return opened == 0




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

    open = [i for i in brackets if i == "<"]
    close = [i for i in brackets if i == ">"]
    if len(open) == len(close):
        return True
    else:
        return False


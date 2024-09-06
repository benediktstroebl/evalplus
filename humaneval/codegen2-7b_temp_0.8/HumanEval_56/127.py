

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
    openers = "<>"
    closers = "><"
    for opener, closer in zip(openers, closers):
        if not any(opener == c for c in brackets):
            return False
        if not any(closer == c for c in brackets):
            return False
    return

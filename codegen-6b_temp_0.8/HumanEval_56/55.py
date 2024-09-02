

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
    # <i>
    # <yes>
    # <yes>
    # <yes>
    # <no>
    # true
    # __________
    # <true>
    # true
    # <yes>
    # true
    # <yes>
    # <yes>
    # <yes>
    # <true>
    # <yes>
    # <no>
    # <yes>
    # <no>
    # <no>
    # <no>
    # true
    # <no>
    # <no>
    # <no>
    # <no>
    # <true>
    # <no>
    # <no>
    # <no>
    # true
    # <no>
    # <no>
    # <no>
    # <no>
    # true
    # <no>
    # <no>
    # true
    # <no>
    # true
    # <no>
    return "<" not in brackets

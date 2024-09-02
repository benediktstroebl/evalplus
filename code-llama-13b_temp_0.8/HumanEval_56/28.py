

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
    # Don't use lists! We haven't covered them yet.
    # NOTE: There is no point in checking for only '<' or '>' in brackets.
    # e.g. "<<<><>>><>"
    # Corner case: empty string
    if len(brackets) == 0:
        return True
    else:
        # Hint: Use a "flag" to track whether there is an unclosed '<' or '>'
        return _________________


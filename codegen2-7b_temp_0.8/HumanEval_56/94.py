

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
    if not brackets:
        return True
    open_brackets = brackets[0]
    close_brackets = brackets[1:]
    if not open_brackets or not close_brackets:
        return False
    if not open_brackets[0] == close_brackets[0]:
        return False
    return correct_bracketing(close_brackets[1:])



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
    opening = ">"
    closing = "<"
    opening_count = brackets.count(opening)
    closing_count = brackets.count(closing)
    if opening_count == closing_count:
        return True
    else:
        return False





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
    return all(brackets.count(open_br) == brackets.count(close_br) + 1 for (open_br, close_br) in ((">", "<"), (">>", "<<"), ("<>", "<")) if open_br!= close_br)

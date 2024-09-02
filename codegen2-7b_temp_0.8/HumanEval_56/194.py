

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
    c = brackets[0]
    if c!= "<" and c!= ">":
        return False
    return correct_bracketing(brackets[1:-1]) and correct_bracketing(brackets[-1:-1:-1])


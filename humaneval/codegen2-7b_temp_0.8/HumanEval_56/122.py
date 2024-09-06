

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
    brackets = brackets.strip()
    if len(brackets) % 2 == 0:
        raise ValueError("brackets length must be odd")
    for idx,bracket in enumerate(brackets):
        if not bracket in "<>" or not brackets[idx-1] == ">":
            return False
    return



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
    level = 0
    for c in brackets:
        if c == ">":
            if level == 0:
                return False
            else:
                level -= 1
        elif c == "<":
            level += 1
    return level == 0


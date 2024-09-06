

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
    if not brackets or len(brackets) % 2!= 0:
        return False
    i = 0
    opened = 0
    while i < len(brackets):
        if brackets[i] == "<":
            opened += 1
            i += 1
        elif brackets[i] == ">":
            if opened == 0:
                return False
            opened -= 1
            i += 1
        i += 1
    return opened == 0



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
    if brackets == "<>":
        return True
    if brackets[-1] == brackets[0]:
        return False
    for i in range(len(brackets)-1):
        if brackets[i:i+2] != "<>" or not correct_bracketing(brackets[i:i+2]):
            return False
    return True



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
    if brackets == "":
        return True
    if len(brackets) == 1:
        return False
    if brackets[0] == ">" or brackets[1] == "<":
        return False
    if brackets[0] == "<" and brackets[1] == ">":
        return correct_bracketing(brackets[2:])
    return correct_bracketing(brackets[1:])


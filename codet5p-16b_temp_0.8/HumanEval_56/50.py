

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

    opened = []
    for bracket in brackets:
        if bracket == "<":
            opened.append(bracket)
        elif opened == []:
            return False
        elif bracket == ">":
            opened.pop()
    if opened == []:
        return True
    else:
        return False


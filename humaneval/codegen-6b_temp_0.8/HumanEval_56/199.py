

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
    count = 0
    for openBracket in brackets:
        if openBracket == "<":
            count += 1
        elif openBracket == ">":
            count -= 1

    if count == 0:
        return True
    else:
        return False


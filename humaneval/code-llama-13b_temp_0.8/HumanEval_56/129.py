

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
    stack = 0
    for bracket in brackets:
        if bracket == "<":
            stack += 1
        else:
            if stack == 0:
                return False
            else:
                stack -= 1
    return stack == 0


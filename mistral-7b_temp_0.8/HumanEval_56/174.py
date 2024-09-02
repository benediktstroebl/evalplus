

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
    # TODO: Implement this function
    brackets = brackets[::-1]
    opening = 0
    closing = 0
    for i in brackets:
        if i == ">":
            closing += 1
        else:
            opening += 1
    if closing == opening:
        return True
    else:
        return False

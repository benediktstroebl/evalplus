

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
    left = 0
    right = 0

    for i in brackets:
        if i == '<':
            left += 1
        else:
            right += 1

    if left == right:
        return True
    else:
        return False


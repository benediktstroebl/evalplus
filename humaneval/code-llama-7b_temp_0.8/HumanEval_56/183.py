

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
    num_left = 0
    for b in brackets:
        if b == '<':
            num_left += 1
        elif num_left == 0:
            return False
        else:
            num_left -= 1

    return num_left == 0


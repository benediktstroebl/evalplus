

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

    counter = 0
    for ch in brackets:
        if ch == '>':
            if counter == 0:
                return False
            counter -= 1
        else:
            counter += 1

    return counter == 0


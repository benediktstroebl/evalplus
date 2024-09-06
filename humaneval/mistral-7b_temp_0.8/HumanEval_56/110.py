

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
    # TODO: 6.3.1
    # raise NotImplementedError
    count = 0
    for bracket in brackets:
        if bracket == '<':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return count == 0


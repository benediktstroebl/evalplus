

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

    opening = []
    for i in brackets:
        if i == '>':
            opening.append(i)
        else:
            if len(opening) == 0:
                return False
            else:
                opening.pop()
    return len(opening) == 0



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
    for b in brackets:
        if b == '<':
            opening.append(b)
        else:
            if not opening:
                return False
            else:
                opening.pop()
    return True if not opening else False


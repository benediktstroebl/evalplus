

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
    opening = 0
    for b in brackets:
        if b == '<':
            opening += 1
        elif b == '>':
            if opening == 0:
                return False
            opening -= 1

    return opening == 0




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
    for i in brackets:
        if i == '<':
            opening += 1
        elif i == '>':
            opening -= 1
            if opening < 0:
                return False
    return opening == 0

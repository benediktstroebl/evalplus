

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
    opened = []
    for b in brackets:
        if b == '<':
            opened.append(b)
        elif len(opened) == 0:
            return False
        elif b == '>':
            opened.pop()
    if len(opened) == 0:
        return True
    else:
        return False

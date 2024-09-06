

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

    lefts = []
    for char in brackets:
        if char == '<':
            lefts.append(char)
        else:
            if not lefts:
                return False
            lefts.pop()
    return len(lefts) == 0



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

    open = []
    for i, char in enumerate(brackets):
        if char == '<':
            open.append(i)
        if char == '>':
            if not open:
                return False
            open.pop()
    return not open

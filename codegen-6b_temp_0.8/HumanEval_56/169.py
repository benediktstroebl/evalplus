

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
    i = 0
    while i < len(brackets):
        if brackets[i] == '<':
            if i + 1 < len(brackets) and brackets[i + 1] == '>':
                i = i + 2
        else:
            i = i + 1
    return i == len(brackets)


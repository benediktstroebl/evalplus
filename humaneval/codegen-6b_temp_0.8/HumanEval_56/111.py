

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
    # checking if the number of '<' is the same of '>', otherwise there is a
    # unbalanced bracket
    if len(brackets) % 2 != 0:
        return False

    for i in range(0, len(brackets), 2):
        if brackets[i] != '>':
            return False
        elif brackets[i + 1] != '<':
            return False
    return True


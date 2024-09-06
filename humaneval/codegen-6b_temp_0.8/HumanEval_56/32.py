

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
    length = len(brackets)
    table = {
        "<" : ">",
        ">" : "<",
    }

    for i in range(length):
        if table[brackets[i]] != brackets[length - 1 - i]:
            return False
    return True

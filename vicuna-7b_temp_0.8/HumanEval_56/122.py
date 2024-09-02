

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
    open_brackets = set(brackets.lower().split("<>"))
    for i in range(len(open_brackets) - 1):
        if open_brackets[i] != open_brackets[i + 1]:
            return False
    return True

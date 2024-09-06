

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
    n_brackets = len(brackets)
    if n_brackets % 2!= 0:
        return False

    for i in range(n_brackets // 2):
        if brackets[i]!= brackets[n_brackets - 1 - i]:
            return False
    return

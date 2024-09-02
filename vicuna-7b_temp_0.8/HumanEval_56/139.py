

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
    if len(brackets) % 2 != 0:
        return False
    for i in range(len(brackets)):
        if bracket = brackets[i]:
            if bracket != bracket[0] * 2:
                return False
        if i + 1 < len(brackets):
            if bracket != brackets[i + 1][0]:
                return False
    return True

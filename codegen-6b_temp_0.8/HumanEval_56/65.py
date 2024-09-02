

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
    l_count = 0
    r_count = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            l_count += 1
        elif brackets[i] == ">":
            r_count += 1
        if l_count < r_count:
            return False
    return True

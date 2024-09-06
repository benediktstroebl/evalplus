

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

    open_count = 0
    close_count = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            open_count += 1
        elif brackets[i] == ">":
            if close_count < open_count:
                close_count += 1
            else:
                return False
    if close_count == open_count:
        return True
    else:
        return False


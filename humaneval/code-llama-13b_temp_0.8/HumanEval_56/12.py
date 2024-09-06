

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

    depth = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            depth += 1
        else:
            depth -= 1
            if depth == -1:
                return False
    return True




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
    st = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            st += 1
        elif brackets[i] == ">":
            st -= 1
    return st == 0




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
    open_brackets = set(brackets.split("<>"))
    for i in range(len(open_brackets)):
        for j in range(i + 1, len(open_brackets)):
            if open_brackets[i] != open_brackets[j]:
                return False
    return True
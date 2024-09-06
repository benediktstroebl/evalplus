

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
    parentheses = []

    for i in range(len(brackets)):
        if brackets[i] == ">":
            if not parentheses:
                return False
            parentheses.pop()

        else:
            parentheses.append("<")

    return len(parentheses) == 0

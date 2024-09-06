

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

    opening = 0
    closing = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            opening += 1
        if brackets[i] == ">":
            closing += 1
        if opening < closing:
            return False
    return opening == closing


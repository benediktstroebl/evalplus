

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
    """
    record the index of the ">"
    """
    stack = []
    for i, bracket in enumerate(brackets):
        if bracket == '<':
            stack.append(i)
        if bracket == '>':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return True

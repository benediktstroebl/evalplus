

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
    n = len(brackets)
    stack = []
    for i in range(0, n):
        if brackets[i] == '<':
            stack.append(i)
        if brackets[i] == '>':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0



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
    placed = "><"
    openers = "<"
    closers = ">"
    stack = []
    for bracket in brackets:
        if bracket in openers:
            stack.append(bracket)
        if bracket in closers:
            idx = closers.index(bracket)
            if len(stack) > 0:
                if openers[idx] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) <= 0:
        return True
    return False



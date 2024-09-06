

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
    stack = []
    for ch in brackets:
        if ch == ">":
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return len(stack) == 0



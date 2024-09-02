

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
    for c in brackets:
        if c in ('<', '>'):
            if stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


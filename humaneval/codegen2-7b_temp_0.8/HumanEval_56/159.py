

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
        if c == ">":
            if not stack or stack[-1] == "<":
                stack.append(c)
            else:
                stack.pop()
        elif c == "<":
            stack.append(c)
    return not stack

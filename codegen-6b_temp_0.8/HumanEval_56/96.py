

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
    for b in brackets:
        if b == ">":
            if not stack or stack[-1] == "<":
                stack.append(b)
            elif stack[-1] != ">":
                stack.append(b)
        elif b == "<":
            if not stack or stack[-1] == ">":
                stack.append(b)
            elif stack[-1] != "<":
                stack.append(b)

    return not stack


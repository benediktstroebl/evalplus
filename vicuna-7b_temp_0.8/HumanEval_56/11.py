

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
    for bracket in brackets:
        if bracket == "<":
            stack.append(1)
        elif bracket == ">":
            stack.append(0)
        elif bracket == "]":
            if not stack:
                return False
            if stack[-1] == 0:
                stack.pop()
                return False
            if stack[-1] == 1:
                stack.pop()
                return False
    return True


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
        if not stack or stack[-1] == c:
            stack.append(c)
        else:
            if stack[-1] == ">" and c == "<":
                stack.pop()
            else:
                return False
    return len(stack) == 0

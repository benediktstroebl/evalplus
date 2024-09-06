

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
        if ch == "<":
            stack.append(ch)
        elif ch == ">":
            if not stack or stack[-1] != "<":
                return False
            stack.pop()
    return True


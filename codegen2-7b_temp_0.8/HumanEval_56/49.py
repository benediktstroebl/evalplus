

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
    if len(brackets) % 2!= 0:
        return False

    stack = []
    for ch in brackets:
        if ch == "<":
            if stack and stack[-1] == ">":
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    if not stack:
        return True
    else:
        return False


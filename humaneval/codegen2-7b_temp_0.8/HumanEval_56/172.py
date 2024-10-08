

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
    if len(brackets) % 2:
        return False
    stack = []
    for c in brackets:
        if c == "<":
            stack.append(c)
        elif c == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return len(stack) ==

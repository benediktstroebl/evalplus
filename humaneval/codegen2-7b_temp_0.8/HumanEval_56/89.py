

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
    assert(len(brackets) % 2 == 0)
    stack = []
    for c in brackets:
        if c == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return len(stack) == 0

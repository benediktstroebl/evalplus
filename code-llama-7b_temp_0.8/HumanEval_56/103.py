

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
    for i, c in enumerate(brackets):
        if c == ">":
            if stack == [] or stack[-1] != "<":
                return False
            stack.pop()
        else:
            stack.append(c)
    return stack == []

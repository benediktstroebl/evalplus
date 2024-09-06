

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
    for char in brackets:
        if char == "<":
            if len(stack) == 0 or stack[-1] == ">":
                return False
            stack.append(char)
        else:
            stack.pop()
    return len(stack) == 0

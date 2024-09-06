

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
        if not stack:
            stack.append(char)
        else:
            if char == "<" and stack[-1] == ">":
                stack.pop()
            else:
                stack.append(char)
    return not stack

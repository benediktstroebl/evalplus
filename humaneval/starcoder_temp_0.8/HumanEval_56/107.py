

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
    # Fill in the rest of the function
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        if char == ">":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

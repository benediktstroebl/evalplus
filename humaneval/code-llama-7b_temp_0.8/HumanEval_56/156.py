

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
    # keep track of open brackets with a stack
    stack = []
    for char in brackets:
        if char == '<':
            stack.append('<')
        else:
            if len(stack) == 0:
                return False
            # if not found, then pop
            stack.pop()
    return len(stack) == 0


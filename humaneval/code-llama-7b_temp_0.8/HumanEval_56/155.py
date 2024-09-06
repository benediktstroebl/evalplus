

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
    # Your code here
    stack = []
    for b in brackets:
        if b == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        elif b == "<":
            stack.append("<")
        else:
            return False
    return len(stack) == 0


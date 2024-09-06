

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
    openers = ["<"]
    closers = [">"]
    stack = []
    for char in brackets:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True







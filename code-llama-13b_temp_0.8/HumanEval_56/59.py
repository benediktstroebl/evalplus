

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
    # make sure brackets are even length
    if len(brackets) % 2 != 0:
        return False
    # can use a stack to check if every opening bracket has a closing bracket
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        if char == ">":
            if len(stack) == 0:
                return False
            if stack.pop() != "<":
                return False
    return len(stack) == 0




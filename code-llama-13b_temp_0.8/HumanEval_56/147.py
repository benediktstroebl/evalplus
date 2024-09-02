

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

    """
    I thought about going through the string backwards (starting at the end), and if I encounter
    an open bracket, I can pop it and go on with the rest of the string. When I encounter a closed
    bracket, I should pop the last element from a stack (which I'm using to track open brackets).
    If I encounter a closed bracket but the stack is empty, or I encounter an open bracket and the
    stack is full, then I should return False.
    """
    stack = []
    for char in brackets:
        if char == ">":
            if not stack:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack




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
    if not brackets:
        return True

    stack = []
    for bracket in brackets:
        if not stack or stack[-1] == "<":
            stack.append(bracket)
        elif stack[-1] == ">":
            stack.pop()
        else:
            stack.pop()
            stack.append(bracket)
    return not stack

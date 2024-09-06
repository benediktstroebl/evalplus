

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
    for i in brackets:
        if i == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                stack.append(i)
        elif i == "<":
            if stack and stack[-1] == ">":
                stack.pop()
            else:
                stack.append(i)

    return len(stack) == 0

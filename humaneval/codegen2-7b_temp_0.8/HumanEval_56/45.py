

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
    opening = ["<", "(", "{", "["]
    closing = [">", ")", "}", "]"]
    stack = []

    for c in brackets:
        if c in opening:
            stack.append(c)
        elif c in closing:
            if stack and c == opening[closing.index(stack[-1])]:
                stack.pop()
            else:
                return False
    return not stack

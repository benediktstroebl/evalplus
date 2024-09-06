

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

    # maintain a stack of "remaining opening brackets"
    # every time we see a closing bracket, we pop the stack
    # if the stack is empty, the bracketing is incorrect
    # if the stack contains an opening bracket with the same kind
    # as the closing bracket, then that's OK
    # otherwise, we got a stray closing bracket

    stack = []  # a stack of opening brackets
    for b in brackets:
        if b == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                return False
        else:
            stack.append(b)
    return len(stack) == 0


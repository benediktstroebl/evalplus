

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
    # # Wrong Answer.
    # stack = []
    # for b in brackets:
    #     if b == '<':
    #         stack.append(b)
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         elif stack.pop()!= '<':
    #             return False
    # return len(stack) == 0

    # Better Answer.
    stack = []
    for b in brackets:
        if b == '<':
            stack.append(b)
        else:
            if len(stack) == 0 or stack.pop()!= '<':
                return False
    return len(stack) == 0

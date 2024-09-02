

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
    # *** YOUR CODE HERE ***

    # Possible answer:
    # stack = []
    # for s in brackets:
    #     if s == '>':
    #         if not stack or stack[-1] != '<':
    #             return False
    #         stack.pop()
    #     else:
    #         stack.append(s)
    # return not stack

    # Another answer:
    stack = []
    for s in brackets:
        if s == '>' and stack and stack[-1] == '<':
            stack.pop()
        else:
            stack.append(s)
    return not stack


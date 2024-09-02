

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
    # Open = 0
    # Close = 0
    # for i in brackets:
    #     if i == "<":
    #         Open += 1
    #     elif i == ">":
    #         Close += 1

    # return Open == Close

    stack = []
    for i in brackets:
        if i == ">":
            if not stack:
                return False
            stack.pop()
        elif i == "<":
            stack.append("<<")

    return len(stack) == 0


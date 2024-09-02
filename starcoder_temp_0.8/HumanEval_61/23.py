

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    # # Wrong version: this one doesn't have a base case!
    # if not brackets:
    #     return True

    # stack = []

    # for b in brackets:
    #     if b == "(":
    #         stack.append(b)
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         stack.pop()

    # return len(stack) == 0


    # Stack version
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

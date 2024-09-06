

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
    # Hint: Use a stack to keep track of opening brackets

    # my_stack = []

    # for bracket in brackets:
    #     if bracket == '<':
    #         my_stack.append(bracket)
    #     else:
    #         if not my_stack:
    #             return False
    #         if my_stack.pop() == '<':
    #             continue
    #         else:
    #             return False

    # if my_stack:
    #     return False
    # else:
    #     return True

    # shorter:

    my_stack = []

    for bracket in brackets:
        if bracket == '<':
            my_stack.append(bracket)
        else:
            if not my_stack or my_stack.pop() == '<':
                continue
            else:
                return False

    return not my_stack



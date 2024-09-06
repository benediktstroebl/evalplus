

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
    #%%
    # Brute-force implementation:
    #
    # Note that we use a list as a stack.
    # append: add to the end
    # pop: remove from the end

    stack = []

    # for each character in the string
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False
    #%%
    # Efficient implementation:
    #
    # Note that we use a list as a stack.
    # append: add to the end
    # pop: remove from the end

    stack = []

    # for each character in the string
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False
    # return len(stack) == 0


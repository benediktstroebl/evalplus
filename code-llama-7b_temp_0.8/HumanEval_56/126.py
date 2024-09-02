

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

    # we'll use a stack to keep track of our opening brackets
    stack = []

    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            # if there are no opening brackets on the stack, we have a mismatch
            if len(stack) == 0:
                return False
            else:
                # remove the last opening bracket from the stack
                stack.pop()

    # we've reached the end, so if the stack is empty we have a match
    return len(stack) == 0


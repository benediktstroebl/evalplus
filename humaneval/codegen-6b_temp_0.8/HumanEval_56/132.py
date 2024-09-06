

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
    # use a stack to store the opening bracket
    stack = []

    # for every bracket in the string
    for bracket in brackets:

        # if it's a "<"
        if bracket == "<":

            # add it to the stack
            stack.append("<")

        # or if it's a ">"
        elif bracket == ">":

            # if the stack is empty
            if len(stack) == 0:

                # return false
                return False

            # otherwise
            else:

                # pop the last element from the stack (it's the top)
                top = stack.pop()

                # if the top element doesn't match the bracket
                if top != "<":

                    # return false
                    return False

    # if the stack is still not empty, there's an unclosed "<"
    if len(stack) > 0:

        # return false
        return False

    # otherwise
    else:

        # return true
        return True

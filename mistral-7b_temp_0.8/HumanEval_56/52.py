

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
    # a stack to store brackets
    stack = []

    # for every bracket in the input string
    for bracket in brackets:
        # if the bracket is a left bracket, add it to the stack
        if bracket == "<":
            stack.append(bracket)
        # if the bracket is a right bracket, remove and compare the top item from the stack
        elif bracket == ">":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    # if the stack is empty after processing all brackets, the brackets are correctly bracketed
    return len(stack) == 0


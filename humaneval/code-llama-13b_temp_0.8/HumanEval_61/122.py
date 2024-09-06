

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
    # make a stack
    stack = []
    # iterate through the brackets
    for bracket in brackets:
        # if it's an opening bracket
        if bracket == '(':
            # push it on the stack
            stack.append(bracket)
        # if it's a closing bracket
        elif bracket == ')':
            # if the stack is empty, there's no opening bracket to match the closing
            if not stack:
                return False
            # pop off the top of the stack
            # if it's not an opening bracket, we're in trouble
            if stack.pop() != '(':
                return False

    # if the stack is empty when we're done, we're in good shape
    if not stack:
        return True
    # but if there's anything left on the stack,
    # there's an opening bracket with no closing bracket
    return False


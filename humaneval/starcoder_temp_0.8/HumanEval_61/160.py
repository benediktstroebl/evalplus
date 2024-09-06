

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
    # make a stack of open brackets
    stack = []
    # iterate through the string
    for c in brackets:
        # if the char is an open bracket, add it to the stack
        if c == '(':
            stack.append(c)
        # if the char is a close bracket, check if there's an opening bracket
        elif c == ')':
            # if there's an open bracket
            if stack:
                # pop that open bracket off the stack
                stack.pop()
            else:
                # if there isn't, then there's a problem
                return False
    # return True if we made it through without a problem
    return True

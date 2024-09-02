

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
    # Your code here
    # use a stack
    # if we see a closing bracket, pop. If we see a openning bracket, push it onto the stack
    # at the end of the function if the stack is empty, then everything is good, otherwise bad
    stack = []
    for i in brackets:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


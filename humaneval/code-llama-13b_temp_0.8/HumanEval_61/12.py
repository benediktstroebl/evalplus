

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

    """
    idea:
    keep a stack. each time you get an opening bracket, push the index to the stack.
    each time you get a closing bracket, pop from the stack.
    if the stack is empty, there is no matching opening bracket for the closing bracket.
    if the stack is not empty, the popped value is the index of the matching opening bracket.
    """

    stack = []
    for i, c in enumerate(brackets):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                return False
    return True




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
    # this function uses stacks
    stack = []
    for c in brackets:
        if c == "(":
            stack.append(c)
        if c == ")":
            if stack:
                stack.pop()
            else:
                return False
    return not stack


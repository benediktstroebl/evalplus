

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
    if not brackets:
        return True
    stack = []
    for bracket in brackets:
        if not stack or stack[-1] == '(' and bracket!= ')':
            stack.append(bracket)
        else:
            stack.pop()
            if not stack:
                return False
    return len(stack) == 0

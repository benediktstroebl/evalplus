

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
    "*** YOUR CODE HERE ***"
    if not brackets:
        return True
    stack = []
    for i, bracket in enumerate(brackets):
        if bracket == '(':
            stack.append(i)
        elif bracket == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


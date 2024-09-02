

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
    stack = []
    for x in brackets:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top == '(':
                top = stack.pop()
                if top!= ')':
                    return False
    return len(stack) == 0

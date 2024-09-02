

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
    # Hint: Use a stack.
    if len(brackets) % 2 != 0:
        return False

    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
        else:
            raise ValueError('Only "(" and ")" allowed')

    if len(stack) != 0:
        return False

    return True

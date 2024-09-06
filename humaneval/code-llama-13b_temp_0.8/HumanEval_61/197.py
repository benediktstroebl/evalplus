

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




    if len(brackets) == 0:
        return True

    stack = []

    for b in brackets:
        if b == '(':
            stack.append(b)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    return len(stack) == 0




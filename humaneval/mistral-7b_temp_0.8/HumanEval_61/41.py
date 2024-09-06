

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
    # TODO

    stack = []
    for c in brackets:
        if c == '(':
            stack.append(')')
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0


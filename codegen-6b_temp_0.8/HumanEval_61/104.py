

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
    stack = []

    for c in brackets:
        if c == '(':
            stack.append(')')
        elif c == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0


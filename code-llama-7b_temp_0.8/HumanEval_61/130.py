

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
    # Loop invariant: stack is either empty or begins with the first unclosed opening bracket.
    stack = []
    for c in brackets:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False
    return stack == []


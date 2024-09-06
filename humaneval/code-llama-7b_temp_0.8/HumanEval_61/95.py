

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
    paren_stack = []
    for c in brackets:
        if c == '(':
            paren_stack.append(c)
        elif c == ')':
            if not paren_stack:
                return False
            paren_stack.pop()
    if paren_stack:
        return False
    return True


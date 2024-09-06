

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
    brace_stack = []
    for brace in brackets:
        if brace == '(':
            brace_stack.append('(')
        elif brace == ')':
            if len(brace_stack) == 0:
                return False
            else:
                brace_stack.pop()
    return len(brace_stack) == 0


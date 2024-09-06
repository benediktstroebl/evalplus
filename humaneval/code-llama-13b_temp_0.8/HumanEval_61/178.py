

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

    s = []
    for c in brackets:
        if c == '(':
            s.append('(')
        else:
            if not s:
                return False
            s.pop()
    return not s

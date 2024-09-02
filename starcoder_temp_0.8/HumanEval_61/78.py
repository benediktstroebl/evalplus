

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
    bracket_stack = []
    for c in brackets:
        if c == "(":
            bracket_stack.append(c)
        elif c == ")":
            if not bracket_stack:
                return False
            bracket_stack.pop()
    return not bracket_stack

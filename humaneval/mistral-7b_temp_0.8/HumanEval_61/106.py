

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
    for bracket in brackets:
        if bracket == '(':
            bracket_stack.append(bracket)
        elif bracket == ')':
            if not bracket_stack:
                return False
            bracket_stack.pop()
    if bracket_stack:
        return False
    return True


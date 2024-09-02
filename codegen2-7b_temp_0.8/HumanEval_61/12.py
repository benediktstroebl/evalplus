

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
    for char in brackets:
        if char == '(':
            bracket_stack.append(char)
        elif char == ')':
            if not bracket_stack:
                return False
            else:
                bracket_stack.pop()
    return not bracket

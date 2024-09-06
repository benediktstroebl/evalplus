

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
    if not brackets:
        return True

    bracket_stack = []
    for i, c in enumerate(brackets):
        if c == "(":
            bracket_stack.append(c)
        else:
            try:
                bracket_stack.pop()
            except IndexError:
                return False
    return len(bracket_stack) == 0

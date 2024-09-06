

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
    stack = []
    for i, br in enumerate(brackets):
        if br == '(':
            stack.append(br)
        else:
            try:
                assert br == stack.pop()
            except IndexError:
                return False
    return len(stack) ==

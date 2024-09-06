

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    bracket_stack = []
    # loop over the index
    for i, c in enumerate(brackets):
        if c == '>':
            if not bracket_stack:
                return False
            if bracket_stack[-1] != '<':
                return False
            bracket_stack.pop()
        else:
            bracket_stack.append('<')
    return len(bracket_stack) == 0



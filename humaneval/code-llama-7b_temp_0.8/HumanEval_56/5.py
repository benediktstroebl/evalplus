

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

    # Use a stack to keep track of unmatched opening brackets

    bracket_stack = []
    for b in brackets:
        if b == '<':
            bracket_stack.append('<')
        elif b == '>':
            if not bracket_stack:
                return False
            if bracket_stack[-1] != '<':
                return False
            bracket_stack.pop()
    return not bracket_stack


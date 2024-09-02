

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
    for b in brackets:
        if b == '>':
            if bracket_stack:
                bracket_stack.pop()
            else:
                return False
        else:
            bracket_stack.append(b)
    return not bracket_stack


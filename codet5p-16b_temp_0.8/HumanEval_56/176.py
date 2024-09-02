

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

    
    open_stack = []
    for c in brackets:
        if c == '<':
            open_stack.append(c)
        elif c == '>':
            if not open_stack:
                return False
            else:
                open_stack.pop()
    return not open_stack




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
    assert len(brackets) % 2 == 0
    stack = []
    for c in brackets:
        if c == '<':
            if len(stack) == 0:
                return False
            stack.pop()
        else:
            stack.append(c)
    return len(stack) ==

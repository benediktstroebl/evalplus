

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
    if not brackets:
        return True
    if brackets[0] != '<':
        return False
    if brackets[-1] != '>':
        return False
    stack = []
    for b in brackets:
        if b == '>':
            if not stack:
                return False
            stack.pop()
        else:
            stack.append(b)
    return not stack


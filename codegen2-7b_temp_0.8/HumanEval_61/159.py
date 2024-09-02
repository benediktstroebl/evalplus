

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
    opening = '({['
    closing = '}])'
    stack = []
    for char in brackets:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            last = stack.pop()
            if char!= opening[closing.index(last)]:
                return False
    return not

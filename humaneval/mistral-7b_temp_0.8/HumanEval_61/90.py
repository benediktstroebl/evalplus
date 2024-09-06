

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
    for c in brackets:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack or stack[-1] != "(":
                return False
            else:
                stack.pop()
        else:
            return False
    if stack:
        return False
    return True




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
    for b in brackets:
        if b == ")":
            while stack:
                if stack[-1] != "(":
                    return False
                stack.pop()
        elif b == "(":
            stack.append(b)
    return not stack

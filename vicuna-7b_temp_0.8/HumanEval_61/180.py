

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
    for char in brackets:
        if char == "(":
            stack.append((False, 1))
        elif char == ")":
            if not stack:
                return False
            top = stack[-1]
            if not top[1]:
                return False
            stack.pop()
        else:
            if stack and stack[-1][0]:
                stack.pop()
    return not stack

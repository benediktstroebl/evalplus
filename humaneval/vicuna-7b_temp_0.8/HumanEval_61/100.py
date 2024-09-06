

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
    # Use a stack to keep track of the open brackets
    stack = []

    for char in brackets:
        if char == "(":
            stack.append(0)
        elif char == ")":
            if not stack:
                return False
            stack[-1] += 1

    return not stack
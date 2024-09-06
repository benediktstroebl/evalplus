

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
    for i in brackets:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


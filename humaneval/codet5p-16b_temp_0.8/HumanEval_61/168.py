

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
            stack.append("(")
        elif i == ")":
            if len(stack) == 0:
                return False
            if stack[-1] == "(":
                stack.pop()
    return len(stack) == 0


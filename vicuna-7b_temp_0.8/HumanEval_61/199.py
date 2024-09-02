

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
        if b == "(":
            stack.append(0)
        elif b == ")":
            if len(stack) == 0:
                return False
            if stack[-1] != 0:
                return False
            stack.pop()
        else:
            stack.append(int(b))
    return stack.pop() == 0
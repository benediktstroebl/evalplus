

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
            stack.append(1)
        elif b == "(":
            stack.append(0)
        else:
            if stack:
                if stack[-1] == 0:
                    return False
                elif stack[-1] == 1:
                    stack.pop()
                else:
                    return False
    return True



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
    for bracket in brackets:
        if bracket == "(":
            stack.append("(")
        elif bracket == ")":
            try:
                if stack.pop() != "(":
                    return False
            except:
                return False
    if len(stack) != 0:
        return False
    else:
        return True

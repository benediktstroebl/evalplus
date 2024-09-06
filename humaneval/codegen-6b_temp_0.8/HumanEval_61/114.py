

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
    index = 0
    while index < len(brackets):
        if brackets[index] == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        index += 1

    if len(stack) > 0:
        return False
    else:
        return True

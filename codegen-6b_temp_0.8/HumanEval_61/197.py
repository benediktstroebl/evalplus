

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
    if len(brackets) % 2 != 0:
        return False
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == "(" and len(stack) == 0:
            stack.append(i)
        elif brackets[i] == ")" and len(stack) > 0:
            stack.pop()
        elif brackets[i] == "(" and len(stack) > 0:
            return False
        elif brackets[i] == ")" and len(stack) == 0:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

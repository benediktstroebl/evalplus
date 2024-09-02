

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
    # check if there are both opening and closing brackets
    if len(brackets) == 0:
        return True
    if len(brackets) % 2 == 1:
        return False
    # make a stack
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == "(":
            stack.append(brackets[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True


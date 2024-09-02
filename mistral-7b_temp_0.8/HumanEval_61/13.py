

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

    opening = '('
    closing = ')'
    opening_index = 0
    closing_index = 0
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == opening:
            stack.append(i)
        if brackets[i] == closing:
            if len(stack) == 0:
                return False
            else:
                opening_index = stack.pop()
                closing_index = i
                if closing_index - opening_index == 2:
                    return True
                else:
                    return False

    return False

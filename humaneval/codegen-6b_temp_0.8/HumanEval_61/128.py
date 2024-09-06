

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
    for i in range(len(brackets)):
        bracket = brackets[i]
        if bracket in "()":
            stack.append(bracket)
        else:
            if bracket == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()

    return not len(stack)

import doctest
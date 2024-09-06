

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
    # brackets_stack = []
    # for bracket in brackets:
    #     if bracket == '(':
    #         brackets_stack.append('(')
    #     elif bracket == ')':
    #         if len(brackets_stack) == 0:
    #             return False
    #         brackets_stack.pop()
    # if len(brackets_stack) != 0:
    #     return False
    # return True

    # second version
    brackets_stack = []
    for bracket in brackets:
        if bracket == '(':
            brackets_stack.append('(')
        elif bracket == ')':
            if len(brackets_stack) == 0:
                return False
            elif brackets_stack[-1] == '(':
                brackets_stack.pop()
            else:
                return False
    if len(brackets_stack) != 0:
        return False
    return True


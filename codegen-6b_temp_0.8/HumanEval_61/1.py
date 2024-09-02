

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
    """
    first_index = []
    bracket_stack = []
    for i, b in enumerate(brackets):
        if b == '(':
            first_index.append(i)
        elif b == ')':
            if len(bracket_stack) == 0:
                return False
            bracket_stack.pop()
    if len(bracket_stack) != 0:
        return False
    return True
    """
    """
    bracket_stacks = []
    for i in range(0, len(brackets)):
        if brackets[i] == '(':
            bracket_stacks.append(')')
        elif brackets[i] == ')':
            if len(bracket_stacks) != 0:
                pop_item = bracket_stacks.pop()
            else:
                return False
    return len(bracket_stacks) == 0
    """
    """
    bracket_stack = []
    for i in range(len(brackets)):
        if brackets[i] == '(':
            bracket_stack.append(')')
        elif brackets[i] == ')' and len(bracket_stack) != 0:
            bracket_stack.pop()
    return len(bracket_stack) == 0
    """
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(')')
        if bracket == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
    
    
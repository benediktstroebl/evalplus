

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
    bracket_stack = []
    close_to_open = {')': '(', ']': '[', '}': '{'}
    for bracket in brackets:
        if bracket == '(':
            bracket_stack.append(bracket)
        elif bracket == '{' or bracket == '[' or bracket == ')':
            if len(bracket_stack) == 0:
                return False
            elif bracket_stack[-1] not in close_to_open:
                return False
            else:
                bracket_stack.pop()
    if len(bracket_stack) == 0:
        return True
    else:
        return False
    

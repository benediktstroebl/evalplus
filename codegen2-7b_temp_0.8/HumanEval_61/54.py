

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
    brackets_list = list(brackets)
    bracket_stack = []
    for bracket in brackets_list:
        if not bracket in ['(', ')']:
            continue
        if bracket == '(':
            bracket_stack.append(bracket)
        else:
            if not bracket_stack or bracket_stack.pop()!= '(':
                return False
    return not bracket

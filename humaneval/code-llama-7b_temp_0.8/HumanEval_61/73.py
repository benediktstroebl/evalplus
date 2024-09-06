

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
    if len(brackets) == 1:
        return False
    open_to_close = {
        '(': ')',
        ')': '(',
    }
    open_stack = []
    for bracket in brackets:
        if bracket == '(':
            open_stack.append(bracket)
        elif bracket == ')':
            if len(open_stack) == 0:
                return False
            elif open_stack.pop() != '(':
                return False
    return len(open_stack) == 0


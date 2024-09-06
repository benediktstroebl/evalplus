

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
    bracket_dict = {'(': ')', '[': ']', '{': '}'}
    bracket_stack = []

    for b in brackets:
        if b in bracket_dict:
            bracket_stack.append(b)
        else:
            if bracket_stack and bracket_dict[bracket_stack[-1]] == b:
                bracket_stack.pop()
            else:
                return False

    return not bracket_stack

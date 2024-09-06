

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
    valid_brackets = set(['(', ')'])
    bracket_stack = []
    for bracket in brackets:
        if bracket in valid_brackets:
            bracket_stack.append(bracket)
        elif bracket == ')' and bracket_stack[-1] == '(':
            del bracket_stack[-1]
        else:
            return False
    return len(bracket_stack) == 0


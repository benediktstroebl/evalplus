

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

    # A stack to keep track of opening brackets.
    bracket_stack = []

    # For every bracket in input.
    for b in brackets:
        if b == '(':
            # Push it onto the stack.
            bracket_stack.append(b)
        elif b == ')':
            # Pop the stack if the bracket is a closing bracket.
            if len(bracket_stack) == 0:
                return False
            bracket_stack.pop()
    return len(bracket_stack) == 0


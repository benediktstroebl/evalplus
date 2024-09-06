

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
    for b in brackets:
        if b == "(":
            bracket_stack.append(")")
        elif b == ")":
            if len(bracket_stack) == 0 or bracket_stack.pop() != "(":
                return False
    return len(bracket_stack) == 0

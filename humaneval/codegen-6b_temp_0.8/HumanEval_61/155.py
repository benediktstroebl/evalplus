

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
    # TODO: Implement me, part 2!
    
    bracket_stack = []

    for bracket in brackets:
        if bracket == "(":
            bracket_stack.append(bracket)
        elif bracket == ")":
            if bracket_stack is None:
                return False
            bracket_stack.pop()

    return True if len(bracket_stack) == 0 else False


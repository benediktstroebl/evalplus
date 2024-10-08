

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
    for bracket in brackets:
        if bracket == "(":
            bracket_stack.append(bracket)
        else:
            if bracket_stack:
                bracket_stack.pop()
            else:
                return False
    return False if bracket_stack else True
            

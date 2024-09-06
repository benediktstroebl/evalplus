

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

    opening_bracket_stack = []
    for bracket in brackets:
        if bracket == "(":
            opening_bracket_stack.append(bracket)
        else:
            if opening_bracket_stack:
                opening_bracket_stack.pop()
            else:
                return False
    return not opening_bracket_stack




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

    brackets = "()" + brackets + "()"
    opening_brackets = "("
    closing_brackets = ")"
    opening_bracket_stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            opening_bracket_stack.append(bracket)
        elif bracket in closing_brackets:
            if not opening_bracket_stack:
                return False
            opening_bracket_stack.pop()
    return not opening_bracket_stack


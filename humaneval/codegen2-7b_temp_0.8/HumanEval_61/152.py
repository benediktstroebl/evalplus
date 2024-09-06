

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
    close_brackets = ")"
    opening_brackets = "("
    bracket_stack = []
    for i in brackets:
        if i == close_brackets[0]:
            bracket_stack.pop()
        elif i == opening_brackets[0]:
            bracket_stack.append(i)
    return len(bracket_stack) == 0

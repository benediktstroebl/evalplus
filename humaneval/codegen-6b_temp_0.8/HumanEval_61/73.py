

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
    if not brackets:
        return True
    if brackets[0] == ")" or brackets[-1] == "(":
        return False
    bracket_stack = []
    for bracket in brackets:
        if bracket == "(":
            bracket_stack.append(bracket)
        else:
            if not bracket_stack:
                return False
            top_bracket = bracket_stack.pop()
            if top_bracket != "(":
                return False
    return not bracket_stack



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

    brackets = list(brackets)
    bracket_stack = []
    for bracket in brackets:
        if bracket == "(":
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) > 0:
                bracket_stack.pop()
            else:
                return False

    return len(bracket_stack) == 0

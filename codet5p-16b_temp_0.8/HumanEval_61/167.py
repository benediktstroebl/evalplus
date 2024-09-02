

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

    open_brackets_stack = []
    for bracket in brackets:
        if bracket == "(":
            open_brackets_stack.append(bracket)
        elif bracket == ")":
            if not open_brackets_stack:
                return False
            else:
                open_brackets_stack.pop()
    return not open_brackets_stack

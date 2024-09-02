

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
    [['()', True], "[]", "{}"]
    stack = []
    for bracket in brackets:
        if bracket in '([{':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            last_bracket = stack.pop()
            if not matches(last_bracket, bracket):
                return False

    return len(stack) == 0


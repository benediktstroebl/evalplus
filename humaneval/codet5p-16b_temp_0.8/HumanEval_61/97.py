

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

    opening = set(brackets)
    stack = []
    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        else:
            if not stack:
                return False
            last_open_bracket = stack.pop()
            if bracket!= ")":
                return False
            if last_open_bracket!= "(":
                return False
    if stack:
        return False
    return True

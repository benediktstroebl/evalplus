

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
    if brackets == '':
        return True

    first_bracket = brackets[0]

    if first_bracket == '(':
        if brackets[-1] == ')':
            return correct_bracketing(brackets[1:-1])

    elif first_bracket == ')':
        if brackets[-1] == '(':
            return correct_bracketing(brackets[1:-1])

    return False


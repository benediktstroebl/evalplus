

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

    if len(brackets) < 2:
        return True
    if brackets[0] == ')' or brackets[-1] == '(':
        return False
    for i in range(1, len(brackets) - 1):
        if brackets[i] == ')' and brackets[i - 1]!= '(' or brackets[i] == '(' and brackets[i + 1]!= ')':
            return False
    return correct_bracketing(brackets[1:-1])

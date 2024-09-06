

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
    if brackets.count('(') != brackets.count(')'):
        return False
    if not brackets:
        return True
    if brackets.count('(') != 0 and brackets.index('(') > brackets.index(')'):
        return False
    return correct_bracketing(brackets[1:])


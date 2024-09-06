

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
    unmatched = []
    for bracket in brackets:
        if bracket == '(':
            unmatched.append(bracket)
        elif unmatched:
            unmatched.pop()
        else:
            return False
    return not unmatched


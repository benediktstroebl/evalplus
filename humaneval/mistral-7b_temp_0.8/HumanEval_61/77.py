

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

    s = brackets.replace('(', ' ( ')
    s = s.replace(')', ') )')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace(' ', '')

    if s:
        return False
    else:
        return True


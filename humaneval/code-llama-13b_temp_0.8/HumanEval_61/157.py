

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
    result = True
    k = 0
    for i in brackets:
        if i == '(':
            k += 1
        elif i == ')':
            if k == 0:
                result = False
            else:
                k -= 1
    if k == 0:
        return result
    else:
        return False


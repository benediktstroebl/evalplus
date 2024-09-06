

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

    flag = 0
    for b in brackets:
        if b == '(':
            flag += 1
        if b == ')':
            flag -= 1
        if flag < 0:
            return False
    return flag == 0




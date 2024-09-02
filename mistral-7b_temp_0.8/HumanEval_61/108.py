

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
    # write your code here
    i = 0
    j = len(brackets) - 1
    while i <= j:
        if brackets[i] == '(':
            if brackets[j] == ')':
                i += 1
                j -= 1
            else:
                return False
        else:
            return False
    return True




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
    if len(brackets) == 0:
        return True
    elif len(brackets) % 2 != 0:
        return False
    else:
        i = 0
        j = 1
        while i < len(brackets) and j < len(brackets):
            if brackets[i] == '(' and brackets[j] == ')':
                i += 1
                j += 1
            else:
                return False
        return True
    
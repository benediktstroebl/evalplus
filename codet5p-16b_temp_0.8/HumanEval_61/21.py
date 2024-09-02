

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

    bracketing = list(brackets)

    if len(bracketing) % 2!= 0:
        return False

    if bracketing[0]!= '(' or bracketing[-1]!= ')':
        return False

    open_bracketing = [i for i in range(len(bracketing)) if bracketing[i] == '(']
    close_bracketing = [i for i in range(len(bracketing)) if bracketing[i] == ')']

    if len(open_bracketing)!= len(close_bracketing):
        return False

    for i in range(len(open_bracketing)):
        if open_bracketing[i] == close_bracketing[i]:
            continue
        else:
            return False

    return True


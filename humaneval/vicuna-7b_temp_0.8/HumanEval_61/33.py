

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
    return all(matched for matched in [(x,y) for x,y in zip(brackets, brackets[1:]) if x == '(' and y == ')'] if x == '(' and y == ')'] if x == '(' and y == ')'])

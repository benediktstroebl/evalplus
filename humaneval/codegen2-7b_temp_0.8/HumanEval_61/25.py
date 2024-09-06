

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
    if len(brackets) % 2!= 0:
        return False
    opening_brackets = "(" * int(len(brackets)/2)
    for i in range(len(brackets)//2):
        if brackets[i]!= opening_brackets[-i-1]:
            return False
    return True



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

    if brackets[0] == ")" or brackets[-1] == "(" or len(brackets) == 0:
        return False
    
    index = 0
    count = 0
    while index < len(brackets):
        if brackets[index] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
        index += 1
    return count == 0


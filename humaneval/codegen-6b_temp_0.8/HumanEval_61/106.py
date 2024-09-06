

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
    "*** YOUR CODE HERE ***"
    i = 0
    while i < len(brackets):
        if brackets[i] == "(":
            if i == len(brackets) - 1:
                return False
            if brackets[i+1] == ")":
                return False
            i += 1
        else:
            if i == 0:
                return False
            if brackets[i-1] == "(":
                return False
        i += 1
    return True


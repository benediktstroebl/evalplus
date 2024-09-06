

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
    if len(brackets) == 0:
        return True
    if len(brackets) % 2 != 0:
        return False
    while brackets:
        left_bracket = brackets[0]
        if left_bracket == "(":
            brackets = brackets[1:]
        elif left_bracket == ")":
            brackets = brackets[2:]
    if len(brackets) == 0:
        return True
    else:
        return False

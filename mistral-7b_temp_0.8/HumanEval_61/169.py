

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
    # WRITE YOUR CODE HERE
    if brackets == "":
        return True
    if brackets[0] == "(":
        return correct_bracketing(brackets[1:])
    else:
        return correct_bracketing(brackets[:-1]) and brackets[-1] == ")"



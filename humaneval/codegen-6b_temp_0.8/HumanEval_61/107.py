

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
    correct_bracket = []
    for i in range(len(brackets)):
        if brackets[i] == "(":
            correct_bracket.append(")")
        else:
            correct_bracket.append("(")

    return correct_bracket == list(brackets)

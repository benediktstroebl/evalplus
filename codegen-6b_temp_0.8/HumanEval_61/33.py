

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
    index = 0
    open_bool = True
    brackets = list(brackets)
    while index < len(brackets):
        if brackets[index] == "(":
            open_bool = False
        else:
            if not open_bool:
                return False
        index += 1
    return open_bool

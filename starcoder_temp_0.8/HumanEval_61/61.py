

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

    # Base case
    if len(brackets) == 0:
        return True
    
    # Checks if the first bracket is opening
    if brackets[0] == "(":
        # Calls itself with the first and second element
        # Eliminates first element from the string
        return correct_bracketing(brackets[1:])
    elif brackets[0] == ")":
        # If the first bracket is closing, calls itself
        # with the first element eliminated
        return correct_bracketing(brackets[1:])
    else:
        return False

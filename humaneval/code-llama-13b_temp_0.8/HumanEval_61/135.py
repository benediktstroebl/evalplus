

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

    # Hint: If you think this can be done with a stack,
    # try using a list as a stack.

    # check if all opening brackets have a closing bracket
    for x in range(len(brackets)):
        # if we find an opening bracket and the next bracket is not a closing bracket
        if brackets[x] == "(" and brackets[x + 1] != ")":
            return False
        # if we find a closing bracket and the previous bracket is not an opening bracket
        if brackets[x] == ")" and brackets[x - 1] != "(":
            return False
    # if we go through the whole string and nothing is wrong, then the brackets are balanced
    return True

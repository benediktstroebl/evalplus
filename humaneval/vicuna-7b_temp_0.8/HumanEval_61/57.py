

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
    # Use a set to store the opening brackets.
    open_brackets = set(brackets)

    # Iterate through the string.
    for i in range(len(brackets)):
        # If the current bracket is not an opening bracket,
        # it must be a closing bracket.
        if brackets[i] not in open_brackets:
            return False

        # If the next bracket is not an opening bracket,
        # it must be a closing bracket.
        if i < len(brackets) - 1:
            if brackets[i+1] not in open_brackets:
                return False

        # If we have reached the end of the string,
        # and all opening brackets have a corresponding closing bracket,
        # then return True.
        if i == len(brackets)-1:
            return True

    return False
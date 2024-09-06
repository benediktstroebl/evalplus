

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
    current = 0
    while current < len(brackets):
        # PASS
        # check if first bracket is opening
        if brackets[current] == "(":
            current += 1
        else:
            # PASS
            # check if second bracket is closing
            if brackets[current] == ")":
                current += 1
            # PASS
            # return False if there are not equal number of opening and closing brackets
            elif brackets[current] == "(":
                return False

    return True



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
    # count how many brackets were opened in the input
    opened_brackets = 0
    for bracket in brackets:
        if bracket == "(":
            opened_brackets += 1
        # if brackets have not yet been closed,
        # increase the count of opened brackets
        elif bracket == ")":
            if opened_brackets == 0:
                return False
            else:
                opened_brackets -= 1

    # all brackets have been closed
    return opened_brackets == 0


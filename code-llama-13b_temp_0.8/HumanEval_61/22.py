

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
    # return False if brackets is ""
    if brackets == "":
        return False
    
    # keep track of how many left brackets there are
    num_left_brackets = 0

    for bracket in brackets:
        # if we see a "(" then add 1 to the counter
        if bracket == "(":
            num_left_brackets += 1
        # if we see a ")" then subtract 1 from the counter
        elif bracket == ")":
            num_left_brackets -= 1
    
    return num_left_brackets == 0

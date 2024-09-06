

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
    num_of_open_brackets = 0
    for bracket in brackets:
        if bracket == "(":
            num_of_open_brackets += 1
        elif bracket == ")":
            num_of_open_brackets -= 1
            if num_of_open_brackets < 0:
                return False
    return num_of_open_brackets == 0


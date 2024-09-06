

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
    # convert brackets to a list of tuples
    brackets_list = brackets.replace("(", "").replace(")", "").split(",")
    # convert list of tuples to a set of tuples
    brackets_set = set(brackets_list)
    # check if every opening bracket has a corresponding closing bracket
    for open_bracket in brackets_set:
        if open_bracket not in brackets_set:
            return False
    return True

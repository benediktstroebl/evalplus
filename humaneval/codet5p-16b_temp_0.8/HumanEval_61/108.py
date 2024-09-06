

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

    brackets_dict = {}

    for bracket in brackets:
        if bracket in brackets_dict.keys():
            brackets_dict[bracket] += 1
        else:
            brackets_dict[bracket] = 1

    for bracket in brackets_dict.keys():
        if brackets_dict[bracket] == 0:
            return False
        else:
            if brackets_dict[bracket] % 2!= 0:
                return False
    return True

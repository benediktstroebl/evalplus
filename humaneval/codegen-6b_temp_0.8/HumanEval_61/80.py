

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
    brackets_used = dict()
    for bracket in brackets:
        if bracket not in brackets_used:
            brackets_used[bracket] = 0
        brackets_used[bracket] += 1
    for bracket, count in brackets_used.items():
        if bracket == ")" and count != 0:
            return False
    return True

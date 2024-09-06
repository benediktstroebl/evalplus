

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
    if len(brackets) < 2:
        return True

    start = 0
    end = len(brackets) - 1
    while start < end:
        if brackets[start] == ")" and brackets[end] == "(":
            start += 1
            end -= 1
        else:
            return False
    return True

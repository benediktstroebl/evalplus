

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

    # total count of brackets
    count = 0

    # count the number of opening brackets
    for bracket in brackets:
        if bracket == '(':
            count += 1

    # count the number of closing brackets
    for bracket in brackets:
        if bracket == ')':
            count -= 1

    # return True if count is equal to zero
    return count == 0


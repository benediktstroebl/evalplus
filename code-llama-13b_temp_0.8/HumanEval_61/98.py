

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

    brackets_list = []
    for bracket in brackets:
        brackets_list.append(bracket)

    opening_count = 0
    for bracket in brackets_list:
        if bracket == "(":
            opening_count += 1
        elif bracket == ")":
            if opening_count == 0:
                return False
            else:
                opening_count -= 1
    if opening_count == 0:
        return True


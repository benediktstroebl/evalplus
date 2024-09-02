

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
    bracket_list = [bracket for bracket in brackets]
    assert len(bracket_list) % 2 == 0, "Not even number of brackets"
    stack = []
    for bracket in bracket_list:
        if bracket == ")":
            if len(stack) == 0:
                return False
            stack.pop()
        else:
            stack.append(bracket)
    return len(stack) ==

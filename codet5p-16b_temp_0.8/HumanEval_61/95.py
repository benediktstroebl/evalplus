

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

    brackets_list = list(brackets)

    if not brackets_list:
        return False

    brackets_stack = []

    for bracket in brackets_list:
        if bracket == "(":
            brackets_stack.append(bracket)
        elif bracket == ")":
            if len(brackets_stack) == 0:
                return False
            elif brackets_stack.pop()!= "(":
                return False

    return True if len(brackets_stack) == 0 else False


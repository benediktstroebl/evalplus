

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

    if len(brackets_list) % 2 == 1:
        return False

    brackets_stack = []
    for bracket in brackets_list:
        if bracket == ")":
            if brackets_stack == []:
                return False
            else:
                brackets_stack.pop()
        elif bracket == "(":
            brackets_stack.append(bracket)

    return brackets_stack == []


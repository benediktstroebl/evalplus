

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

    open_brackets = "("
    closed_brackets = ")"
    brackets_list = list(brackets)
    open_brackets_stack = []
    for index, bracket in enumerate(brackets_list):
        if bracket == open_brackets:
            open_brackets_stack.append(index)
        elif bracket == closed_brackets:
            if len(open_brackets_stack) == 0:
                return False
            open_index = open_brackets_stack.pop()
            if open_index == index - 1:
                continue
            else:
                return False

    return len(open_brackets_stack) == 0


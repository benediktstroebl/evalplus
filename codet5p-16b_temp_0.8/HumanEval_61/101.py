

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

    brackets_stack = []
    for br in brackets:
        if br == "(":
            brackets_stack.append(br)
        else:
            if len(brackets_stack) == 0:
                return False
            else:
                brackets_stack.pop()
    return len(brackets_stack) == 0

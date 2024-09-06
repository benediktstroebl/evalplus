

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
    for c in brackets:
        if c == "(":
            brackets_stack.append(c)
        else:
            if brackets_stack:
                brackets_stack.pop()
            else:
                return False
    return not brackets_stack

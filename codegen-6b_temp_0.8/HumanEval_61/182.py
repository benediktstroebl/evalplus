

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
    if not len(brackets):
        return True
    stack = []
    for i in brackets:
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
                stack.append(i)
            except IndexError:
                return False
    return not len(stack)

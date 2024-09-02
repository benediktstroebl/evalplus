

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
    stacks = []
    for char in brackets:
        if char == '(':
            stacks.append(char)
        else:
            if not stacks:
                return False
            stacks.pop()
    if stacks:
        return False
    return True

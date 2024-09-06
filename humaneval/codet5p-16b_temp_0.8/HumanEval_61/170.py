

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

    open_stack = []
    for char in brackets:
        if char == "(":
            open_stack.append(char)
        elif char == ")":
            if len(open_stack) == 0:
                return False
            open_stack.pop()

    return len(open_stack) == 0

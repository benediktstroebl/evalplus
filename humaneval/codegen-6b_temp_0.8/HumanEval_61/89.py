

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
    bracket_stack = Stack()
    for b in brackets:
        if b == "(":
            bracket_stack.push("(")
        elif b == ")":
            if bracket_stack.is_empty():
                return False
            else:
                bracket_stack.pop()
    return bracket_stack.is_empty()


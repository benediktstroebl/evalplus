

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
    parens_stack = []
    for char in brackets:
        if char == "(":
            parens_stack.append(char)
        elif char == ")":
            if len(parens_stack) == 0:
                return False
            parens_stack.pop()
    return len(parens_stack) == 0


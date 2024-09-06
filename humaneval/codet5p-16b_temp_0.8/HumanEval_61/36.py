

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

    stack: list = []
    for bracket in brackets:
        if bracket == ")":
            try:
                top = stack.pop()
            except:
                return False
            if top!= "(":
                return False
        else:
            stack.append(bracket)
    return len(stack) == 0

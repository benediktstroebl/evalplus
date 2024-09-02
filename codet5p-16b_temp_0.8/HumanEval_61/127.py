

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

    stack = []
    for b in brackets:
        if b == ")":
            try:
                assert stack.pop() == "("
            except:
                return False
        elif b == "(":
            stack.append("(")
        else:
            return False
    return len(stack) == 0

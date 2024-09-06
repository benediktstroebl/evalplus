

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

    # Hint: Use a stack.

    # TODO: Edit this line
    stack = []

    # TODO: Edit this line
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        if bracket == ")":
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True


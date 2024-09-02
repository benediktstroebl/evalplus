

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
    """
    # Wrong Answer
    open_brackets = 0
    for bracket in brackets:
        if bracket == "(":
            open_brackets += 1
        elif bracket == ")":
            open_brackets -= 1
        if open_brackets < 0:
            return False
    return open_brackets == 0
    """
    # Right Answer
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0

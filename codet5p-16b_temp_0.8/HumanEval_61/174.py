

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

    open_brackets = "("
    close_brackets = ")"

    stack = []
    for bracket in brackets:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if len(stack) == 0 or stack.pop()!= bracket:
                return False
    return len(stack) == 0

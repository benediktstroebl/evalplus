

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # create a stack
    stack = []
    # track if we've seen anything in the opening bracket
    opening_bracket = "("
    closing_bracket = ")"
    # loop through the string
    for i in range(len(brackets)):
        if brackets[i] == opening_bracket:
            stack.append(i)
        elif brackets[i] == closing_bracket:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


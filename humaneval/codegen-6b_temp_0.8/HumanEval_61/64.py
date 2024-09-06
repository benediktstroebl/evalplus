

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
    is_balanced = True
    index = 0
    while index < len(brackets):
        if brackets[index] == "(":
            stack.append("(")
        elif brackets[index] == ")":
            if len(stack) == 0:
                is_balanced = False
            else:
                stack.pop()

        index += 1

    return is_balanced and len(stack) == 0




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

    # count = brackets.count("(")
    # count2 = brackets.count(")")
    # if count == count2:
    #     return True
    # else:
    #     return False

    stack = []
    for symbol in brackets:
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


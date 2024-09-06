

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
    opening = '('
    closing = ')'
    stack = []

    for bracket in brackets:
        if bracket == opening:
            stack.append(bracket)
        elif bracket == closing:
            if stack == []:
                return False
            else:
                stack.pop()
        else:
            raise ValueError("invalid bracket: {}".format(bracket))

    return stack == []


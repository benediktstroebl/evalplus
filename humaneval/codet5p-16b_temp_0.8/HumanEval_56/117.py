

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

    if len(brackets) == 0:
        return True

    if len(brackets) == 1:
        return False

    # do a simple check
    if brackets[0]!= '<':
        return False

    if brackets[-1]!= '>':
        return False

    opening_brackets_stack = []

    for bracket in brackets:
        if bracket == '<':
            opening_brackets_stack.append(bracket)
        else:
            if not opening_brackets_stack:
                return False
            opening_brackets_stack.pop()

    return True




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

    pairs = {")": "("}
    stack = []
    for bracket in brackets:
        if bracket not in pairs:
            stack.append(bracket)
        else:
            if len(stack) == 0 or stack.pop()!= pairs[bracket]:
                return False
    return len(stack) == 0


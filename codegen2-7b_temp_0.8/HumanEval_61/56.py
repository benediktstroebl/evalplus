

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
    if len(brackets) % 2!= 0:
        return False
    pairs = list(zip(brackets[::2], brackets[1::2]))
    stack = []
    for left, right in pairs:
        if left == "(" and right == ")":
            if len(stack) == 0:
                return False
            stack.pop()
        else:
            stack.append(left)
    return len(stack



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

    brackets_stack = []

    for b in brackets:
        if b == "(":
            brackets_stack.append(b)
        elif b == ")":
            if not brackets_stack:
                return False
            brackets_stack.pop()
        else:
            raise ValueError(f"unexpected character {b}")

    if brackets_stack:
        return False
    return True


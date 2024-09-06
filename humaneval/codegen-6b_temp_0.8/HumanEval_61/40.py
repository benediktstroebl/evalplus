

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
    while brackets:
        if brackets.startswith("()"):
            brackets = brackets[2:]
        elif brackets.startswith(")("):
            brackets = brackets[2:]
        elif brackets.startswith(")("):
            brackets = brackets[2:]
        else:
            return False
    return True
    # or use the following code when you think of a more elegant solution:
    # return True if len(brackets) % 2 == 0 else False

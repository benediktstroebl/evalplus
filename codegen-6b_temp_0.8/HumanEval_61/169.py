

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
    brackets = brackets[1:-1]
    while brackets:
        left, right = brackets[0], brackets[-1]
        if left == ")":
            return False
        elif right == "(":
            brackets = brackets[1:-1]
        else:
            brackets = "".join(brackets[1:-1])
    return True



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
    # base cases
    if len(brackets) == 0:
        return True
    if len(brackets) % 2!= 0:
        return False

    # split into two parts
    left, right = brackets[:len(brackets) // 2], brackets[len(brackets) // 2:]
    return (left.count("(") == left.count(")") and
            right.count("(") == right.count(")"))




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

    # base case
    if len(brackets) == 1:
        return True

    brackets_left = brackets.replace("()", "")
    brackets_right = brackets.replace("()", "")
    if len(brackets_right)!= 0:
        return False
    elif brackets_left[0] == ")" or brackets_left[-1] == "(":
        return False
    return correct_bracketing(brackets_left[1:-1])

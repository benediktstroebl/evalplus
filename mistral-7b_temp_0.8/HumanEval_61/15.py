

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

    # your code here
    open = 0
    close = 0

    for char in brackets:
        if char == "(":
            open += 1
        elif char == ")":
            close += 1

    if open == close:
        return True
    else:
        return False


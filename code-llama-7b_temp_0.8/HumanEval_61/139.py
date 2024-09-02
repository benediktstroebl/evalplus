

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

    # List to keep track of open brackets
    open_brackets = []

    for bracket in brackets:
        if bracket == '(':
            open_brackets.append(bracket)
        else:
            if len(open_brackets) == 0:
                return False
            else:
                open_brackets.pop()

    if len(open_brackets) == 0:
        return True
    else:
        return False


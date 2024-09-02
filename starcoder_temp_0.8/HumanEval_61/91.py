

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

    open_brackets = []

    for char in brackets:
        if char == "(":
            open_brackets.append(char)
        elif char == ")":
            if open_brackets == []:
                return False
            else:
                open_brackets.pop()

    if open_brackets == []:
        return True
    else:
        return False

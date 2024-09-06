

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
    index = 0
    while index < len(brackets):
        if brackets[index] == "(":
            index += 1
        elif brackets[index] == ")":
            index += 1
            if index == len(brackets):
                return True
            while index < len(brackets) and brackets[index] != "(":
                index += 1
        else:
            return False
    if index == len(brackets):
        return True
    return False


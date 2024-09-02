

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
    brackets = list(brackets)
    index = 0
    while index < len(brackets):
        if brackets[index] == "(":
            brackets.pop(index)
        elif brackets[index] == ")":
            brackets.pop(index)
        else:
            index += 1
    return len(brackets) == 0

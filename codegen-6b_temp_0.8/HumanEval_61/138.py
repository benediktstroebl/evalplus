

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
    matching_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == "(":
            matching_brackets.append(")")
        if brackets[i] == ")":
            if len(matching_brackets) == 0:
                return False
            matching_brackets.pop()
    return len(matching_brackets) == 0

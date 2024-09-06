

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
    opening_brackets = []
    for index in range(len(brackets)):
        if brackets[index] == "(":
            opening_brackets.append("(")
        elif brackets[index] == ")":
            if len(opening_brackets) == 0:
                return False
            else:
                opening_brackets.pop()
    return len(opening_brackets) == 0

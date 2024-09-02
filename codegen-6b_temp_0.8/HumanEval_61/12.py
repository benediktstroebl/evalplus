

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
    correct_brackets = []

    for bracket in range(len(brackets)):
        if brackets[bracket] == "(":
            correct_brackets.append(bracket)
        elif len(correct_brackets) > 0:
            correct_brackets.pop()

    return len(correct_brackets) == 0

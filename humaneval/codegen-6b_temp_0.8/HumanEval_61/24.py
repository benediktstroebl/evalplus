

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
    left_brackets = []
    for i, bracket in enumerate(brackets):
        if bracket == "(":
            left_brackets.append(i)
        elif bracket == ")" and not left_brackets:
            return False
    right_brackets = []
    for i in range(len(brackets) - 1, -1, -1):
        if brackets[i] == ")":
            right_brackets.append(i)
        elif brackets[i] == "(" and not right_brackets:
            return False
    return True

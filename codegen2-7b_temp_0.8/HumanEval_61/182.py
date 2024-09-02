

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

    for index, bracket in enumerate(brackets):
        if bracket not in "({[":
            return False

        if index!= len(brackets) - 1:
            if brackets[index + 1]!= bracket:
                return False
    return True


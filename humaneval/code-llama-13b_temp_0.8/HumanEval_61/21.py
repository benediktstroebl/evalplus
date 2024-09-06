

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

    # Hint: Keep track of the number of unmatched opening brackets.
    # If you reach the end of the string and there are still unmatched
    # opening brackets then the brackets are not balanced.
    # print(brackets)

    if not len(brackets):
        return True

    if brackets[0] == "(":
        return correct_bracketing(brackets[1:])

    if not len(brackets) >= 2:
        return False

    if brackets[1] == ")" and brackets[0] == "(":
        return correct_bracketing(brackets[2:])

    if brackets[1] == ")" and brackets[0] != "(":
        return False

    if brackets[0] != "(":
        return False

    return False


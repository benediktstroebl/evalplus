

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
    # Hint: Keep track of how many unmatched "(" you've seen so far.
    # Hint: Take a look at the first and last characters.
    if not brackets:
        return True

    if brackets[0] == "(":
        return False

    if brackets[0] == ")":
        return False

    if len(brackets) % 2 == 0:
        return correct_bracketing(brackets[1:len(brackets) - 1])

    return False


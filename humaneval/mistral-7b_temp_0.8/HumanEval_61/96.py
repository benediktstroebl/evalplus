

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

    # Write your solution here.
    def is_correct_bracketing(brackets):
        if brackets == "":
            return True
        if len(brackets) == 1:
            return False
        if brackets[0] == ")":
            return False
        if brackets[0] != "(":
            return False
        if brackets[-1] == ")":
            return is_correct_bracketing(brackets[:-1])
        return is_correct_bracketing(brackets[1:-1])

    return is_correct_bracketing(brackets)


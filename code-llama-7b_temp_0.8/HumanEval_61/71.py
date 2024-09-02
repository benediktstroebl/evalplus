

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

    def helper(idx, num_open):
        if idx == len(brackets):
            return num_open == 0

        if brackets[idx] == "(":
            num_open += 1
            return helper(idx + 1, num_open)
        if brackets[idx] == ")":
            num_open -= 1
            return helper(idx + 1, num_open)

    return helper(0, 0)


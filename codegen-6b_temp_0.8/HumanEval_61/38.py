

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
    def is_balanced(position: int):
        if position == len(brackets):
            return True
        else:
            if brackets[position] == "(":
                return is_balanced(position + 1)
            else:
                return is_balanced(position + 1)

    if len(brackets) == 0:
        return True
    else:
        return is_balanced(0)


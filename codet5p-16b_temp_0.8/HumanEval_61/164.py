

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

    opening = []
    closing = []
    for i in brackets:
        if i == "(":
            opening.append(i)
        elif i == ")":
            closing.append(i)
        else:
            raise ValueError("Invalid bracketing")

    if len(opening) == len(closing) == 0:
        return True
    else:
        return len(opening) == len(closing)


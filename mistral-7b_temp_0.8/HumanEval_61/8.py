

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
    brackets = brackets.strip(" ")
    if brackets == "":
        return True
    if brackets.count("(") != brackets.count(")"):
        return False
    left = 0
    for bracket in brackets:
        if bracket == "(":
            left += 1
        else:
            if left == 0:
                return False
            left -= 1
    return True


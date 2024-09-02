

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
    opening_brackets = "([{"
    closing_brackets = ")]}"

    opened_brackets = []

    for bracket in brackets:
        if bracket in opening_brackets:
            opened_brackets.append(bracket)
        elif bracket in closing_brackets:
            if opened_brackets and closing_brackets.index(bracket) == opened_brackets[-1].index(opening_brackets[0]):
                opened_brackets.pop()
            else:
                return False

    return not opened_brackets




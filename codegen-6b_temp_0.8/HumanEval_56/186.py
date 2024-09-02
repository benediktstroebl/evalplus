

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    opening_brackets = []

    for index, bracket in enumerate(brackets):
        if bracket == "<":
            opening_brackets.append(index)

    closing_brackets = []

    for index, bracket in enumerate(brackets[::-1]):
        if bracket == ">":
            closing_brackets.append(len(brackets) - index - 1)

    # we want to make sure that the indices match.
    for index, opening in enumerate(opening_brackets):
        closing = closing_brackets[index]
        if opening != closing:
            return False

    return True

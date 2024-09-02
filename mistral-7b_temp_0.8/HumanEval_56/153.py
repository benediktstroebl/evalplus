

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
    closing_brackets = []

    for bracket in brackets:
        if bracket == '<':
            opening_brackets.append(bracket)
        elif bracket == '>':
            closing_brackets.append(bracket)

    if len(opening_brackets) != len(closing_brackets):
        return False

    return all(opening_bracket == closing_bracket for (opening_bracket, closing_bracket) in zip(opening_brackets, closing_brackets))



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
    bracket_list = list(brackets)
    opening_brackets = []
    closing_brackets = []
    for bracket in bracket_list:
        if bracket == "<":
            opening_brackets.append("<")
        if bracket == ">":
            closing_brackets.append(">")

    opening_brackets.sort()
    closing_brackets.sort()
    return opening_brackets == closing_brackets[::-1]


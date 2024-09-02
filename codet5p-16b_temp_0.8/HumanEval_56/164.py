

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
        if bracket == "<":
            opening_brackets.append(bracket)
        else:
            assert bracket == ">"
            if len(opening_brackets) == 0:
                return False
            closing_brackets.append(bracket)
            opening_brackets.pop()

    return len(opening_brackets) == 0

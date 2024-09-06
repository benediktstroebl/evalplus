

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

    # return True if every opening bracket has a corresponding closing bracket
    opening_brackets = ["<"]
    closing_brackets = [">"]
    for bracket in brackets:
        if bracket in opening_brackets:
            opening_brackets.remove(bracket)
            closing_brackets.append(bracket)
        elif bracket in closing_brackets:
            closing_brackets.remove(bracket)
    return True if len(opening_brackets) == 0 and len(closing_brackets) == 0 else False


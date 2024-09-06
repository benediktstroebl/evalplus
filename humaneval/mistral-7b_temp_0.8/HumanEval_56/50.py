

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
    opening_brackets = ["<", ">", "!", "(", ")", "{"]
    closing_brackets = ["<", ">", "!", ")", "(", "}"
    bracket_dict = {"<": ">", ">": "<", "!": "!", "(": ")", ")" : "("}
    opening_bracket = []
    closing_bracket = []
    for bracket in brackets:
        if bracket in opening_brackets:
            opening_bracket.append(bracket)
        elif bracket in closing_brackets:
            closing_bracket.append(bracket)
    opening_bracket.reverse()
    if opening_bracket == closing_bracket:
        return True
    else:
        return False


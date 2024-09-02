

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
    opening_brackets = '()[]{}'
    closing_brackets = ')][}'

    bracket_dict = {bracket: bracket for bracket in opening_brackets}
    bracket_dict.update({
        bracket: opening_bracket for opening_bracket, bracket in zip(opening_brackets, closing_brackets)
    })

    stack = []
    for bracket in brackets:
        if bracket in bracket_dict:
            stack.append(bracket)
        elif stack and stack[-1] == bracket_dict[bracket]:
            stack.pop()
        else:
            return False

    return True if not stack else False


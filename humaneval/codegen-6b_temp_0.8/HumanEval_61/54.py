

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
    opening_parentheses = []
    for index, char in enumerate(brackets):
        if char == "(":
            opening_parentheses.append(index)
            
    closing_parentheses = []
    for index, char in enumerate(brackets[::-1]):
        if char == ")":
            closing_parentheses.append(len(brackets) - index - 1)

    opening_parentheses_in_closing = [
        idx for idx, val in enumerate(closing_parentheses)
        if val in opening_parentheses
        ]

    return len(opening_parentheses_in_closing) == len(opening_parentheses)

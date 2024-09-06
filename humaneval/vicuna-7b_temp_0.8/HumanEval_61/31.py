

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
    # Convert the string of parentheses to a list of open and close bracket pairs
    brackets = [bracket for open_bracket, close_bracket in zip(brackets.split(), brackets[1:].split(',')) if open_bracket == '(']

    # Check if every open bracket has a corresponding close bracket
    for open_bracket in brackets:
        if not any(close_bracket in open_bracket for close_bracket in brackets):
            return False
    return True

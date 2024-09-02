

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

    # Hint: Keep track of the number of unmatched opening brackets
    # as you go through the string. If the string starts with an
    # opening bracket, then you'll never be able to close it.

    if brackets[0] == '(':
        return False
    if brackets[len(brackets) - 1] == ')':
        return False

    opening_bracket_count = 0
    closing_bracket_count = 0

    for char in brackets:
        if char == '(':
            opening_bracket_count += 1
        elif char == ')':
            if opening_bracket_count == 0:
                return False
            opening_bracket_count -= 1
        closing_bracket_count += 1
    if opening_bracket_count == 0 and closing_bracket_count == len(brackets):
        return True
    return False




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
    
    # Find the closing (
    opening_bracket_index = brackets.index("(")

    # Find the second closing bracket
    opened = True
    for i, char in enumerate(brackets):
        if char == "(":
            opened = False
        elif char == ")" and not opened:
            closing_bracket_index = i
            break
    
    # Check the brackets are balanced
    if opening_bracket_index != closing_bracket_index:
        return False
    
    return True

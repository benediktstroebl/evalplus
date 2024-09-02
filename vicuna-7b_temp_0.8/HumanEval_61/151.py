

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
    for opening_brace in brackets:
        for i in range(1, len(opening_brace)):
            if opening_brace[0] == '(' and not (opening_brace[i-1] == '(' and opening_brace[i] == ')') or \
               opening_brace[0] == '[' and not (opening_brace[i-1] == '[') and not (opening_brace[i] == ']') or \
               opening_brace[0] == '{' and not (opening_brace[i-1] == '{') and not (opening_brace[i] == '}'):
                return False
    return True

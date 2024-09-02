

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

    
    opening_brackets = []
    for character in brackets:
        if character == "(":
            opening_brackets.append(character)
        elif character == ")":
            if len(opening_brackets) == 0:
                return False
            else:
                opening_brackets.pop()
    if len(opening_brackets)!= 0:
        return False
    else:
        return True

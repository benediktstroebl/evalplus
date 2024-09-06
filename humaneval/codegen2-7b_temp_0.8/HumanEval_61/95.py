

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
    corrected = ""
    for char in brackets:
        if char == "(":
            if corrected!= "":
                corrected += char
        else:
            if corrected == "":
                return False
            elif char!= corrected[-1]:
                return False
            else:
                corrected = corrected[:-1]
    if corrected!= "":
        return False
    return True



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

    if len(brackets) % 2!= 0:
        return False
    else:
        closing_brackets = list()
        for bracket in brackets:
            if bracket == '(':
                closing_brackets.append(')')
            else:
                try:
                    closing_brackets.pop()
                except:
                    return False
    return True


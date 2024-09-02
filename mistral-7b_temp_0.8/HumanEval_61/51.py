

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
    opening_brackets = '()[]{}'
    index = 0
    opening_brackets_index = 0
    for char in brackets:
        if char in opening_brackets:
            opening_brackets_index += 1
            index += 1
        else:
            if opening_brackets_index == 0:
                return False
            opening_brackets_index -= 1
            index += 1

    return index == 0






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
    # Find the index of the first closing bracket.
    opening_count = 0
    for i in range(len(brackets)):
        if bracket = '(':
            opening_count += 1
        elif bracket == ')':
            opening_count -= 1

        if opening_count < 0:
            return False

    # Check that there is only one closing bracket for every opening bracket.
    closing_count = 0
    for i in range(len(brackets)):
        if bracket == '(':
            closing_count += 1
        elif bracket == ')':
            closing_count -= 1

        if opening_count != closing_count:
            return False

    return True

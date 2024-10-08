

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
    # your code here
    open_brackets = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            open_brackets += 1
        elif brackets[i] == ')':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                return False
    return open_brackets == 0




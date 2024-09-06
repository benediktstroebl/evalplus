

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
    # TODO: implement this function!
    counter = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            counter += 1
        elif brackets[i] == ')':
            if counter == 0:
                return False
            else:
                counter -= 1
    return counter == 0


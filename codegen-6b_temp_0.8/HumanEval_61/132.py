

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
    "*** YOUR CODE HERE ***"
    
    open_list = []
    for i in range(len(brackets)):
        if brackets[i] == '(':
            open_list.append(brackets[i])
        else:
            if len(open_list) == 0:
                return False
            else:
                open_list.pop()

    if len(open_list) == 0:
        return True
    else:
        return False




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
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == '(':
            stack.append(brackets[i])
        else:
            if stack == [] or brackets[i]!= stack.pop():
                return False
    return True if stack == [] else False

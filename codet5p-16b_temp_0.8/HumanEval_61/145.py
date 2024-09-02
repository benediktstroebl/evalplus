

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

    opens = []
    for i in range(len(brackets)):
        if brackets[i] == "(":
            opens.append(i)
        elif brackets[i] == ")":
            if opens == []:
                return False
            opens.pop()
    return not opens

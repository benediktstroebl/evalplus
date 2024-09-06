

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
    if not brackets:
        return True
    
    stack = []
    j = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            stack.append(")")
            j = i
        elif brackets[i] == ")":
            if not stack:
                return False
            stack.pop()
        else:
            j = i
    
    return j == len(brackets)-1

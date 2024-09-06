

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
    s = Stack()
    for x in brackets:
        if x == "(":
            s.push(x)
        elif x == ")":
            if s.is_empty():
                return False
            else:
                s.pop()
    if s.is_empty():
        return True
    else:
        return False

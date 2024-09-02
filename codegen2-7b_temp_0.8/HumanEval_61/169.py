

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
    assert len(brackets) % 2 == 0, "length of brackets is not even"
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack or stack.pop()!= '(':
                return False
    return not

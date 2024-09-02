

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

    if brackets[0] == ')' or brackets[0] == '}':
        return False
    if len(brackets) % 2!= 0:
        return False
    stack = []
    for bracket in brackets:
        if bracket == '(' or bracket == '{':
            stack.append(bracket)
        if bracket == ')' or bracket == '}':
            if not stack:
                return False
            last = stack.pop()
            if last == '(' and bracket!= ')':
                return False
            if last == '{' and bracket!= '}':
                return False
    return True if not stack else False



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

    closing_brackets = set([')', ']', '}'])
    stack = []

    for bracket in brackets:
        if bracket in closing_brackets:
            if not stack:
                return False
            if stack.pop()!= bracket:
                return False
        else:
            stack.append(bracket)
    return not stack



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
    flag = True
    stack = []
    for i in brackets:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                flag = False
                break
            else:
                stack.pop()
    if stack:
        flag = False
    return flag

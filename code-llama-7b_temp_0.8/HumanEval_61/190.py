

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
    # My first version
    # return brackets.count('(') == brackets.count(')')

    # My second version
    # if not brackets:
    #     return True
    # stack = []
    # for x in brackets:
    #     if x == '(':
    #         stack.append('(')
    #     elif x == ')':
    #         if not stack:
    #             return False
    #         stack.pop()
    # return not stack

    # My third version
    # if not brackets:
    #     return True
    # stack = []
    # for x in brackets:
    #     if x == ')':
    #         if not stack:
    #             return False
    #         stack.pop()
    #     else:
    #         stack.append('(')
    # return not stack

    # My fourth version
    if not brackets:
        return True
    stack = []
    for x in brackets:
        if x == ')':
            if not stack:
                return False
            stack.pop()
        elif x == '(':
            stack.append('(')
    return not stack




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
    # My solution
    # stack = []
    # for ch in brackets:
    #     if ch == '(':
    #         stack.append(ch)
    #     elif ch == ')':
    #         if not stack:
    #             return False
    #         stack.pop()
    # return not stack

    # My solution: using list comprehension to generate a list of closing brackets that match the last opening bracket
    # Note that stack.pop() will pop the last item in the stack
    # return not [ch for ch in brackets if ch == ')' and not stack.pop()]

    # 10.5 2016Z Luo
    # make a stack
    stack = []
    for ch in brackets:
        # put opening bracket into the stack
        if ch == '(':
            stack.append(ch)
        # if there is closing bracket in the stack
        # and the closing bracket matches the last opening bracket
        elif ch == ')' and stack:
            # remove the opening bracket
            stack.pop()
        # if there is closing bracket in the stack
        # and the closing bracket does not match the last opening bracket
        elif ch == ')':
            # no need to append the closing bracket
            return False
    # if there are still opening brackets in the stack
    # return False
    return not stack


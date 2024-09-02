

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
    # if no opening bracket, there must be no closing bracket, so it must be True
    if brackets.find('(') == -1:
        return True
    # use stack to keep track of "("
    stack = []
    for c in brackets:
        # if "(" is found, append to stack
        if c == '(':
            stack.append('(')
        # if ")" is found
        elif c == ')':
            # if stack is not empty, pop the last "(" from stack
            if stack:
                stack.pop()
            # if stack is empty, return False
            else:
                return False
    # if stack is empty at the end, all "(" has been paired with ")"
    if not stack:
        return True
    # if stack is not empty, return False
    return False


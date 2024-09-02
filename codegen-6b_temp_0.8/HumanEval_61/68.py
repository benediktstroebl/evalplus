

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
    "*** YOUR CODE HERE ***"
    bracket_stack = Stack()
    for i in brackets:
        if i == '(':
            bracket_stack.push(i)
        if i == ')':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    if not bracket_stack.is_empty():
        return False
    return True

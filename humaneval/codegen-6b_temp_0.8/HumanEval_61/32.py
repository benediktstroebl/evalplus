

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
    b_stack = Stack()
    for b in brackets:
        if b == "(":
            b_stack.push("(")
        elif b == ")":
            if b_stack.is_empty():
                return False
            elif b_stack.pop() != "(":
                return False
    return b_stack.is_empty()




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
    my_stack = Stack()
    # create a stack to hold the opening brackets
    for char in brackets:
        # add opening brackets to stack
        if char == "(":
            my_stack.push(char)
        # check that closing brackets match opening brackets
        elif char == ")":
            # if the stack is empty, return false
            if my_stack.is_empty():
                return False
            my_stack.pop()
        # if the stack is not empty, return false
    return my_stack.is_empty()

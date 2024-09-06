

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # use a stack to keep track of opening brackets
    bracket_stack = Stack()
    for char in brackets:
        if char == "<":
            bracket_stack.push(char)
        elif char == ">":
            if bracket_stack.is_empty() == True:
                return False
            else:
                bracket_stack.pop()
    return bracket_stack.is_empty()


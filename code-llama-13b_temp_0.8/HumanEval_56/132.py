

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

    brackets_stack = Stack()
    for b in brackets:
        if b == ">":
            if brackets_stack.pop() is not "<":
                return False
        else:
            brackets_stack.push(b)
    return brackets_stack.is_empty()





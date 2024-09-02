

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

    assert isinstance(brackets, str), "brackets must be a str"
    stack = Stack()
    for b in brackets:
        if b == "<":
            stack.push(b)
        else:
            if stack.is_empty():
                return False
            if stack.pop() != "<":
                return False
    return stack.is_empty()



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
    "*** YOUR CODE HERE ***"
    stack = Stack()
    for b in brackets:
        if b == "<":
            stack.push(b)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()



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

    if len(brackets) % 2 != 0:
        return False

    stack = Stack()
    for bracket in brackets:
        if bracket == "<":
            stack.push(bracket)
        elif bracket == ">":
            if stack.is_empty():
                return False
            else:
                stack.pop()

    return stack.is_empty()


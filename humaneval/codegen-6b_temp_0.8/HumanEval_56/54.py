

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
    MATCH = {")": "(", ">": "<", "<": ">"}
    stack = Stack()
    for b in brackets:
        if b == ">":
            if stack.peek() == "(":
                stack.pop()
            else:
                return False
        else:
            if stack.peek() == ")":
                return False
            stack.push(b)

    return stack.is_empty()


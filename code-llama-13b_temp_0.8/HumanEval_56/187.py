

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

    # make sure that brackets are only "<" or ">"
    for char in brackets:
        if char != "<" and char != ">":
            return False

    stack = Stack()
    for char in brackets:
        if char == "<":
            stack.push(char)
        elif char == ">":
            if not stack.isEmpty():
                if stack.pop() == "<":
                    continue
                else:
                    return False
            else:
                return False

    if stack.isEmpty():
        return True
    else:
        return False


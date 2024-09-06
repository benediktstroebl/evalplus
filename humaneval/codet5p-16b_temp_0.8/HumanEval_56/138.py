

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

    assert len(brackets) % 2 == 0
    open_brackets = {"(", "["}
    close_brackets = {")", "]"}
    stack = []
    for char in brackets:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if open_brackets[last_open]!= char:
                return False
    return len(stack) == 0

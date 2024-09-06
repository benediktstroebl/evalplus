

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
    s = Stack()
    for char in brackets:
        if char in "([{<":
            s.push(char)
        elif not s.is_empty() and s.peek() == char:
            s.pop()
        else:
            return False
    return s.is_empty

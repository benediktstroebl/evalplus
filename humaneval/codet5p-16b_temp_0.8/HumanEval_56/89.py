

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

    brackets_stack = []
    for b in brackets:
        if b == '<':
            brackets_stack.append('>')
        else:
            if not brackets_stack:
                return False
            brackets_stack.pop()

    return not brackets_stack

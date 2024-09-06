

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
            brackets_stack.append(b)
        elif b == '>':
            if len(brackets_stack) == 0 or brackets_stack[-1]!= '<':
                return False
            else:
                brackets_stack.pop()

    if len(brackets_stack) == 0:
        return True
    else:
        return False



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
    open_brackets = {"<": ">", ">": "<"}
    stack = []

    for i, c in enumerate(brackets):
        if c in open_brackets:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if stack[-1]!= open_brackets[c]:
                return False
            stack.pop()

    return len(stack)

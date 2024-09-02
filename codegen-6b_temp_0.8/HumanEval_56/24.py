

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
    map = {"<": ">",
           "}": "{",
           "]": "["}

    stack = []
    for b in brackets:
        if b in '<>':
            if len(stack) == 0:
                return False

            if not is_matching(stack[-1], b):
                return False

            stack.pop()

        else:
            stack.append(b)

    return True

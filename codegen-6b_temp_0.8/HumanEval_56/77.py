

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
    for b in brackets:
        if b == ">":
            stack = []
            for c in brackets:
                if c == "<":
                    stack.pop()
                else:
                    stack.append(">")
            return len(stack) == 0
        elif b == "<":
            stack = []
            for c in brackets:
                if c == ">":
                    stack.pop()
                else:
                    stack.append("<")
            return len(stack) == 0
        else:
            continue
    return True

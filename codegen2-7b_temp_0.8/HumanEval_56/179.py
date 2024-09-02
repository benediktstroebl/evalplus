

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
    brackets = brackets.strip("<>")
    if len(brackets) % 2 == 1:
        return False
    else:
        stack = []
        for c in brackets:
            if c == "<":
                stack.append(c)
            else:
                if not stack:
                    return False
                stack.pop()
        return not stack

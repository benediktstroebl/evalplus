

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

    def is_open(c):
        return c == '<'

    def is_close(c):
        return c == '>'

    def stack_is_empty():
        return len(stack) == 0

    stack = []

    for c in brackets:
        if is_open(c):
            stack.append(c)
        else:
            if stack_is_empty():
                return False
            else:
                last_open = stack.pop()
                if is_close(last_open):
                    continue
                else:
                    return False
    return stack_is_empty()

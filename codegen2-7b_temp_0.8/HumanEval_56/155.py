

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
    open_brackets, close_brackets = brackets.split("<"), ">"
    if len(open_brackets)!= len(close_brackets):
        return False
    stack = []
    for bracket in open_brackets:
        if len(stack) == 0 or bracket!= close_brackets[stack[-1]]:
            stack.append(bracket)
        else:
            stack.pop()
    return len(stack)

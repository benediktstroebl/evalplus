

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
    stack = []
    brace_dict = {"[": "]", "{": "}", "(": ")", "<": ">"}

    for i in brackets:
        if i in brace_dict:
            stack.append(i)
        elif len(stack) == 0:
            return False
        else:
            if i != brace_dict[stack[-1]]:
                return False
            stack.pop()

    if len(stack) > 0:
        return False

    return True

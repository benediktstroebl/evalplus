

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
    opening = {'>': '<', '<': '>', '<<': '>>'}
    stack = []
    for i in brackets:
        if i not in opening:
            if len(stack)!= 0 and stack[-1]!= opening[i]:
                return False
            else:
                stack.append(i)
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

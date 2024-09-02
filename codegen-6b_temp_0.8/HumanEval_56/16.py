

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
    for bracket in brackets:
        if bracket == ">":
            # pop off all "<" and ">"
            while stack and stack[-1] != "<":
                stack.pop()
            # if stack is empty:
            if not stack:
                return False
            # else:
            #   remove last "<"
            else:
                stack.pop()
        else:
            # else:
            #   place < onto stack
            stack.append(bracket)
    # if there are anything left in the stack:
    if stack:
        return False
    # else:
    #   return True
    else:
        return True



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
    # first implement this with loops
    # you can use len(brackets)
    brackets = brackets.replace("<<", "<").replace(">>", ">").replace("<<>", "<>")
    opening = ["<"]
    closing = [">"]
    stack = []
    for i in brackets:
        if i in opening:
            stack.append(i)
        elif i in closing:
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            return False
    return True if len(stack) == 0 else False




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
    # YOUR CODE HERE
    if len(brackets) % 2 != 0:
        return False
    opening = ["<"]
    closing = [">"]
    stack = []
    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack) == 0 or bracket != closing[stack[-1]]:
                return False
            stack.pop()
    return len(stack) == 0


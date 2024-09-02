

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
    # return brackets.count("<") == brackets.count(">")
    # Use a stack instead of a queue, so that we can efficiently pop the last element
    # append/pop on an empty stack is O(1), but on a full stack is O(n)
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if stack:
                stack.pop()
            else:
                return False
    return not stack

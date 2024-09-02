

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
    opening_brackets = {"(": ")", "[": "]", "{": "}"}
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets and len(stack) == 0:
            return False
        elif bracket in closing_brackets:
            if stack.pop() != opening_brackets[bracket]:
                return False
    return len(stack) == 0

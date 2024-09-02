

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
    opening_brackets = ["<", "(", "{"]
    closing_brackets = [">", ")", "}"]

    for b in brackets:
        if b in opening_brackets:
            stack.append(b)
        elif b in closing_brackets:
            if len(stack) == 0:
                return False
            if closing_brackets.index(b) != opening_brackets.index(stack[-1]):
                return False
            stack.pop()

    return len(stack) == 0

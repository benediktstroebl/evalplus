

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

    if len(brackets) < 2:
        return True
    
    opening = {"(", "[", "{"}
    closing = {")", "]", "}"}

    stack = []

    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()
            if bracket!= closing[last_open]:
                return False

    return len(stack) == 0


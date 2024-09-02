

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
    # checking the length of the string
    if len(brackets) % 2 != 0:
        return False

    # the stack to keep the opening brackets
    stack = []

    # iterating over the string and pushing opening brackets to the stack
    for br in brackets:
        if br == '<':
            stack.append(br)
        elif br == '>':
            # if the stack is empty, then we have too many closing brackets
            if not stack:
                return False
            # if the stack is not empty, then we have the right number of opening brackets
            stack.pop()
        else:
            return False

    # if the stack is empty, then we have the right number of opening brackets
    if not stack:
        return True
    # if the stack is not empty, then we have too many opening brackets
    else:
        return False




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

    # (1) initialize the stack
    stack = []

    # (2) for each character in brackets,
    for char in brackets:

        # (2.1) if it's "<",
        if char == "<":

            # (2.1.1) append it to the stack
            stack.append(char)

        # (2.2) else if it's ">",
        elif char == ">":

            # (2.2.1) if the stack is empty, return False
            if not stack:
                return False

            # (2.2.2) otherwise, pop the top element of the stack
            # and compare it with ">"
            # if they don't match, return False
            else:
                if stack.pop() != "<":
                    return False

    # (3) if the stack is empty, return True
    return not stack

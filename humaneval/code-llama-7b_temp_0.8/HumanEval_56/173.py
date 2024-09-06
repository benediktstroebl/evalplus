

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

    def stack_used():
        """
        Returns True if the stack was used to store the brackets.
        """
        return len(stack) > 0

    stack = []

    for char in brackets:
        if char == ">":
            if stack_used():
                stack.pop()
            else:
                return False
        elif char == "<":
            stack.append(char)
    return not stack_used()


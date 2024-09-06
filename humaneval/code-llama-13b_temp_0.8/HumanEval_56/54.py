

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

    # Make a stack for opening brackets.
    stack = Stack()

    # Loop over the characters in the string.
    for b in brackets:

        # If the character is an opening bracket,
        # push it on the stack.
        if b == "<":
            stack.push(b)

        # If the character is a closing bracket,
        # check the stack.
        elif b == ">":

            # If the stack is empty, the brackets are not balanced.
            if stack.is_empty():
                return False

            # If the stack is not empty, pop an opening bracket off the
            # stack. We don't care if it matches the current closing bracket;
            # all we care is whether there is one to match it.
            stack.pop()

    # If the stack is empty, the brackets are balanced.
    return stack.is_empty()

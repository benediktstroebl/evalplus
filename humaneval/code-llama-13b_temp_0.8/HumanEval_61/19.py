

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # Hint: Keep track of the brackets that you have already seen using a stack.
    # Whenever you see a closing bracket, you check the last item in the stack.
    # If it is not an opening bracket, or if the stack is empty, return False.
    # Otherwise, remove the opening bracket from the stack.

    # Hint 2: If the string is empty, return True.
    # If the string is not empty, take the first character.
    # If the character is an opening bracket, add it to the stack.
    # Otherwise, check if the stack is empty, and if the last item in the stack
    # is an opening bracket.
    # If it is, remove it from the stack.
    # Otherwise return False.
    # Then recur on the rest of the string.
    # Don't forget to check for a non-empty stack at the end!
    raise NotImplementedError


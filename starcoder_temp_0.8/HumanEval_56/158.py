

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
    # Beginning at index 0, look through list of brackets, incrementing index as you go,
    #   while storing the current index in a variable called "stack_index".
    # If you encounter a ">" and the index of the last "<" before it is the same as stack_index,
    #   remove those 2 from the list.
    # If you encounter a "<" and there is no ">" before it, add it to the stack.
    # If you encounter a "<" and there is a ">" before it, see if the index of that ">" is
    #   the same as the index of the last "<" on the stack. If they are the same,
    #   then the stack is in correct order and remove both from the list.
    #   If they are different, then the stack is incorrect and return False.
    # If you reach the end of the list, then the stack must have been correct.
    stack_index = 0
    stack = []
    for index, item in enumerate(brackets):
        if item == "<":
            stack.append(index)
        if item == ">":
            if len(stack) == 0:
                return False
            last_index = stack.pop()
            if last_index!= stack_index:
                return False
            stack_index += 1
    if len(stack) > 0:
        return False
    return True

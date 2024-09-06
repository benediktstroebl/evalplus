

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
    # TODO: use stack
    # Brackets are ">","<","[","]","(",")"
    # Check every value ">" and "<" corresponds to a bracket
    # Check brackets using stacks/queues
    # If matches, continue checking
    if brackets == "":
        return True
    if len(brackets) % 2 != 0:
        return False
    stack = []
    for char in brackets:
        if char == ">":
            stack.append("<")
        elif char == "<":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True


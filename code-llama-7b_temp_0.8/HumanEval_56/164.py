

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

    # index the first bracket, so we know where to start
    start = brackets.find("<")

    # if there is no starting point, return False
    if start == -1:
        return False

    # start a stack, use ">" as a marker
    stack = [">"]

    # loop through all brackets
    for i in range(start, len(brackets)):

        # if it's a <, push it onto the stack
        if brackets[i] == "<":
            stack.append("<")

        # if it's a >, pop the stack
        elif brackets[i] == ">":
            stack.pop()

    # if the stack is empty, then we have the correct number of brackets
    if not stack:
        return True
    else:
        return False


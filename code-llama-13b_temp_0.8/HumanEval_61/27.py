

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

    # Hint: Use a stack.

    # first make sure there are only parenthesis in the string
    valid = True
    for char in brackets:
        if char != "(" and char != ")":
            valid = False
            break
    # if there are any other chars in the string then return false
    if not valid:
        return False
    # if there are no parenthesis then the brackets are balanced
    if not brackets:
        return True

    # if the first char is a closing paren return false
    if brackets[0] == ")":
        return False

    # create a stack
    stack = Stack()

    # for every char in the string
    for char in brackets:
        # if it is an open paren
        if char == "(":
            # append to the stack
            stack.push("(")
        # otherwise if it is a closing paren
        else:
            # if there are no items on the stack
            if stack.size() == 0:
                # return false
                return False
            # otherwise
            else:
                # pop the stack
                stack.pop()

    # if there are items left on the stack
    if stack.size() > 0:
        # return false
        return False

    # otherwise
    return True



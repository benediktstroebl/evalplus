

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
    # Copy the string into a list and create a stack to track the open brackets.
    bracket_list = list(brackets)
    stack = []
    last_is_open = False
    # Repeat until the list is empty.
    while len(bracket_list) > 0:
        # Pop input off the list, and see if the next element is a bracket.
        top = bracket_list.pop(0)
        if top == "(":
            # If it is an open bracket, add it to the stack.
            stack.append(top)
            last_is_open = True
        elif top == ")":
            # If it is a closed bracket, and it is an open bracket,
            # then it is in the correct bracketing format.
            if last_is_open and len(stack) > 0:
                stack.pop()
                last_is_open = False
            else:
                return False
        else:
            # Invalid input.
            return False
    # If the stack is empty, and the string has more than one element,
    # then the string is not of the correct form.
    if len(stack) > 0 and last_is_open:
        return False
    return True


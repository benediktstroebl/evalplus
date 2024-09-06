

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
    # these are two stacks
    opening_bracket_stack = []
    closing_bracket_stack = []

    # this is a counter
    count = 0

    # go through each character
    for character in brackets:
        # we check to see if it is a opening bracket
        if character == "<":
            # we add it to the top of the opening stack
            opening_bracket_stack.append(count)
            # we increment our counter
            count += 1
        # if it is a closing bracket
        elif character == ">":
            # we check to see if the opening stack is empty
            if not opening_bracket_stack:
                # if it is, we add it to the closing stack
                closing_bracket_stack.append(count)
            # otherwise, we pop the top of the opening stack and put it on the closing stack
            else:
                opening_bracket_stack.pop()

    # we check to see if the opening stack is empty
    if not opening_bracket_stack:
        # if it is, return true
        return True
    # if it is not, we return false
    else:
        return False


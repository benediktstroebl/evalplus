

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
    # Create an empty array
    stack = []
    # Iterate through the brackets in the string
    for bracket in brackets:
        # If the current bracket is a ">"
        if bracket == ">":
            # If the top of the stack is an "<"
            if len(stack) and stack[-1] == "<":
                # Remove the top of the stack and add the current bracket to the stack
                stack.pop()
                stack.append(bracket)
            # Otherwise, the stack is not empty and there is no "<"
            else:
                # Print an error message
                print("There is no closing bracket for the opening bracket", bracket)
                return False
        # If the current bracket is a "<"
        elif bracket == "<":
            # If the top of the stack is an ">"
            if len(stack) and stack[-1] == ">":
                # Remove the top of the stack and add the current bracket to the stack
                stack.pop()
                stack.append(bracket)
            # Otherwise, the stack is not empty and there is no ">"
            else:
                # Print an error message
                print("There is no opening bracket for the opening bracket", bracket)
                return False

    # If the stack is empty, everything is well-formed
    if len(stack) == 0:
        return True
    # Otherwise, there is no closing bracket for the opening bracket
    else:
        return False

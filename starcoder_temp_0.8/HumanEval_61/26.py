

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

    # make a stack
    # start a for loop and iterate through the bracket string
    # if you see a ( add it to the stack
    # if you see a )
    # if stack is empty return False
    # if stack isn't empty pop it off
    # if the popped off item isn't a ( return False
    # if the popped off item is a ( return True

    stack = []
    for char in brackets:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack == []:
                return False
            else:
                stack.pop()
    return True

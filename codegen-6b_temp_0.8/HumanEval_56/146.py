

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
    
    # going to use a stack to keep track
    stack = []
    
    # for each character in the string
    for c in brackets:
        # if the current character is an opening bracket
        if c == "<":
            # add it to the stack
            stack.append(c)
        elif c == ">":
            # check that the stack is not empty
            if not stack:
                # if the stack is empty, return false
                return False
            # otherwise, pop the last item from the stack
            popped = stack.pop()
            # if the last item in the stack is not the opening bracket
            if popped != "<":
                # return false
                return False

    # if the stack is still not empty, return false
    return not stack

assert correct_bracketing("<")
assert correct_bracketing("<>")
assert correct_bracketing("<<><>>")
assert correct_bracketing("><<>")
assert correct_bracketing("<>><---<><><><") == False
assert correct_bracketing("<<><>") == True
assert correct_bracketing("<><<><>") == False
assert correct_bracketing("<<><>><><>>") == False
assert correct_bracketing("<><<><>") == True

    
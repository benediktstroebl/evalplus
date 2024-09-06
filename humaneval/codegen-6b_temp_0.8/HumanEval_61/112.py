

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
    # iterate over the string, looping if using while
    # compare opening bracket to closing bracket
    # return true if bracket match
    
    # initialise variables
    bracket_stack = Stack()
    open_brackets = "()"

    # iterate over list of brackets
    for i in range(len(brackets)):
        # check if character is an open or a close bracket
        if brackets[i] in open_brackets:
            # push character onto bracket_stack
            bracket_stack.push(brackets[i])
        else:
            # check if stack is empty
            # if it is, return false, the bracket does not match
            if bracket_stack.is_empty():
                return False
            # otherwise, pop last element from bracket stack
            else:
                last_opening = bracket_stack.pop()
                # compare last opening bracket to closing bracket
                if last_opening != brackets[i]:
                    return False

    # if bracket_stack is empty, return true
    if bracket_stack.is_empty():
        return True
    # otherwise return false
    else:
        return False


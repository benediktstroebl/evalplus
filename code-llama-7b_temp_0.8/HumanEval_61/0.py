

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
    #TODO: return True if and only if: 
    stack = []  # a stack of opening brackets that you pop from
    for b in brackets:
        if b == '(': 
            stack.append(b)  # if it is an opening bracket then append to stack
        else:
            if not stack:
                return False  #if no opening bracket available in stack then return false
            stack.pop()  #if it is a closing bracket, then pop from stack
    return not stack  # return True if stack is empty else return False

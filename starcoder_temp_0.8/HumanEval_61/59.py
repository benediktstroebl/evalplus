

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

    # your code here
    #Hint: Python has a stack data structure you can use (https://docs.python.org/3/tutorial/datastructures.html)

    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


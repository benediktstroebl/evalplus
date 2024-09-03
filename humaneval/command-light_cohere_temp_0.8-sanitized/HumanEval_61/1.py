def correct_bracketing(brackets: str): 
    """ Check whether a given brackets string has correct formatting by looking for matching openings and closings.

    Args: 
        - brackets: a string of "(" and ")".

    Returns: 
        - True if the string has correct brackets formatting, False otherwise.

    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()))")
    True
    >>> correct_bracketing(")())")
    True
    >>> correct_bracketing("()()())")
    True
    >>> correct_bracketing(")(()())")
    False
    >>> correct_bracketing("((()))")
    False
    >>> correct_bracketing((())")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == '(': 
            stack.append(True)
        else:
            stack.pop()
   
    stack.append(False)
   
    return stack == []
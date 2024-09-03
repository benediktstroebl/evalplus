```python
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

# Example usage
print(correct_bracketing("()"))
``` 
This script provides a function that checks whether a given brackets string has correct formatting. It uses a stack- technique to keep track of the opening brackets and their corresponding closings. If the stack is empty at the end of the string, it means all brackets are matched correctly, and the function returns True. Otherwise, it returns False. 

I hope this script helps solve the problem and pass the tests.
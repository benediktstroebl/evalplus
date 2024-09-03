```python
def correct_bracketing(brackets):
    """ Checks whether a given string of brackets is balanced.
    Args: brackets (strring of '>' and '<')
    Returns: boolean indicating whether the brackets are balanced. """
    Returns True if every opening bracket has a corresponding closing bracket.
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("{<}>")
    False
    >>> correct_bracketing("()<>")
    True
    >>> correct_bracketing("{[])")
    True
    """

    stack = []
    for bracket in brackets:
        if bracket == '>':
            stack.append(True)
        else:
            stack.append(False)

    return stack == []
```  This function corrects all the brackets in the string. It uses a stack data structure to track the open brackets and uses the stack property to determine if the string is balanced or not.  The bracket and its corresponding opening bracket.
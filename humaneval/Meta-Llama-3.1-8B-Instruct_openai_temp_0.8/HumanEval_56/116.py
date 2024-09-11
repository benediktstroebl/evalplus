```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in the input string has a corresponding closing bracket.

    Args:
    brackets (str): A string consisting of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.

    Example:
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # Initialize a stack to store opening brackets
    stack = []
    
    # Iterate over each character in the input string
    for bracket in brackets:
        # If we encounter an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If we encounter a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, it means there's no corresponding opening bracket for this closing bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, if the stack is empty, it means every opening bracket had a corresponding closing bracket
    # If the stack is not empty, it means there were some opening brackets without corresponding closing brackets
    return not stack

# Test the function
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    
    # Initialize a stack to store opening brackets
    stack = []
    
    # Iterate over the string
    for bracket in brackets:
        # If the bracket is an opening bracket, push it to the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # If the stack is empty after iterating over the string, every opening bracket has a corresponding closing bracket
    # If the stack is not empty, there are some opening brackets without corresponding closing brackets
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
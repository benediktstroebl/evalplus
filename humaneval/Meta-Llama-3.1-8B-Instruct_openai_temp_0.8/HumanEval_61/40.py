```python
def correct_bracketing(brackets: str):
    """
    Check if every opening bracket in the string has a corresponding closing bracket.

    Args:
        brackets (str): A string containing only '(' and ')'.

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to store opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == '(':
            stack.append(bracket)
        # If the character is a closing bracket and the stack is empty, return False
        elif bracket == ')' and not stack:
            return False
        # If the character is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ')' and stack:
            stack.pop()
    
    # After iterating over the entire string, if the stack is empty, return True
    # Otherwise, return False because there are unmatched opening brackets
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack data structure to keep track of the opening brackets encountered in the string. If a closing bracket is encountered and the stack is empty, it means there's no corresponding opening bracket and the function returns False. If the stack is not empty when the entire string has been processed, it means there are unmatched opening brackets and the function returns False. Otherwise, the function returns True.
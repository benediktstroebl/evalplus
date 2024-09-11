```python
def correct_bracketing(brackets: str):
    """
    Checks if a string of "<" and ">" has balanced bracketing.
    
    Args:
    brackets (str): A string consisting of "<" and ">".
    
    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    
    # Initialize an empty stack to store opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, return False because there's no corresponding opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, return True if the stack is empty (all brackets were matched)
    # and False if the stack is not empty (there are unmatched opening brackets)
    return not stack

# Test cases
print(correct_bracketing("<"))  # Should print: False
print(correct_bracketing("<>"))  # Should print: True
print(correct_bracketing("<<><>>"))  # Should print: True
print(correct_bracketing("><<>"))  # Should print: False
```

This script uses a stack data structure to keep track of the opening brackets encountered while iterating over the input string. When a closing bracket is encountered, it checks if the stack is empty (meaning there's no corresponding opening bracket) or pops the opening bracket from the stack. After iterating over the entire string, it returns True if the stack is empty (meaning all brackets were matched) and False otherwise.
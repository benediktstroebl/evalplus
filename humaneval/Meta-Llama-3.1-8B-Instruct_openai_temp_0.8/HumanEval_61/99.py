```python
def correct_bracketing(brackets: str) -> bool:
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
        # If the bracket is an opening bracket, push it onto the stack
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
    
    # After iterating over the string, if the stack is empty, every opening bracket has a corresponding closing bracket
    # So return True
    # If the stack is not empty, there are some opening brackets without corresponding closing brackets, so return False
    return not stack


# Test the function
print(correct_bracketing("("))  # Output: False
print(correct_bracketing("()"))  # Output: True
print(correct_bracketing("(()())"))  # Output: True
print(correct_bracketing(")(()"))  # Output: False
```

This script defines a function `correct_bracketing` that checks if every opening bracket has a corresponding closing bracket in a given string of parentheses. It uses a stack data structure to keep track of the opening brackets and checks if there are any remaining opening brackets after processing the entire string. The script also includes test cases to verify the correctness of the function.
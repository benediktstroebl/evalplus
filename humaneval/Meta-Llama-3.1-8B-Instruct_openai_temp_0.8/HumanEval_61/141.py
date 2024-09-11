```python
def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket in a string has a corresponding closing bracket.

    Args:
        brackets (str): A string containing only "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to store opening brackets
    stack = []

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # After iterating over the entire string, if the stack is empty, every opening bracket had a corresponding closing bracket
    # If the stack is not empty, there were some opening brackets without corresponding closing brackets, so return False
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that takes a string of parentheses as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. It uses a stack to keep track of the opening brackets. After iterating over the entire string, it checks if there are any opening brackets left in the stack, which indicates that there were some opening brackets without corresponding closing brackets.
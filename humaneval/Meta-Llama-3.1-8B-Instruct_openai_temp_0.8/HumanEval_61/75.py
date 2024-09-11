```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
    brackets (str): A string containing only '(' and ')'.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to keep track of the opening brackets

    for bracket in brackets:  # Iterate over each character in the string
        if bracket == '(':  # If the character is an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ')':  # If the character is a closing bracket
            if not stack:  # If the stack is empty, there's no corresponding opening bracket
                return False
            stack.pop()  # Otherwise, pop the corresponding opening bracket from the stack

    return not stack  # After iterating over the entire string, if the stack is empty, every opening bracket had a corresponding closing bracket


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that uses a stack to check if every opening bracket has a corresponding closing bracket in the given string. It then includes test cases to verify the function's correctness.
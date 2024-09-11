```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
        brackets (str): A string of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack
    for bracket in brackets:
        if bracket == "(":  # If a opening bracket is encountered, push it to the stack
            stack.append(bracket)
        elif bracket == ")":  # If a closing bracket is encountered
            if not stack:  # If the stack is empty, return False because there's no corresponding opening bracket
                return False
            stack.pop()  # If the stack is not empty, pop the last opening bracket from the stack
    return not stack  # Return True if the stack is empty (i.e., all opening brackets have a corresponding closing bracket)

# Test cases
print(correct_bracketing("("))  # Expected output: False
print(correct_bracketing("()"))  # Expected output: True
print(correct_bracketing("(()())"))  # Expected output: True
print(correct_bracketing(")(()"))  # Expected output: False
```

This script uses a stack data structure to keep track of the opening brackets encountered in the string. When a closing bracket is encountered, it checks if the stack is empty (i.e., there's no corresponding opening bracket). If the stack is not empty, it pops the last opening bracket from the stack. Finally, it returns True if the stack is empty (i.e., all opening brackets have a corresponding closing bracket) and False otherwise.
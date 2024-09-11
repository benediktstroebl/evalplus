```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Stack to store opening brackets
    stack = []

    # Iterate through each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it into the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket
        elif bracket == ")":
            # If the stack is empty, it means there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # After iterating through the entire string, if the stack is empty, it means every opening bracket has a corresponding closing bracket, so return True
    # If the stack is not empty, it means there are some opening brackets without corresponding closing brackets, so return False
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The function uses a stack to keep track of the opening brackets and their corresponding closing brackets. The test cases at the end demonstrate the function's behavior with different inputs.
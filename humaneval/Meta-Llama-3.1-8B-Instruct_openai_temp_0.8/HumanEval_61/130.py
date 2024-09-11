```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:  # Iterate over the string
        if bracket == "(":  # If we encounter an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ")":  # If we encounter a closing bracket
            if not stack:  # If the stack is empty (no matching opening bracket)
                return False  # Return False
            stack.pop()  # Remove the corresponding opening bracket from the stack

    return not stack  # If the stack is empty after iterating over the string, every opening bracket had a matching closing bracket

# Test the function
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty. If it is, that means there's no matching opening bracket for the current closing bracket, so the function returns False. If the stack is not empty, it removes the top element (the corresponding opening bracket) from the stack. After iterating over the entire string, if the stack is empty, that means every opening bracket had a matching closing bracket, so the function returns True. If the stack is not empty, that means there are some opening brackets without matching closing brackets, so the function returns False.
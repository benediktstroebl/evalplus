```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket in the given string.

    Args:
        brackets (str): A string containing only "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to keep track of opening brackets
    stack = []

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # Otherwise, pop the opening bracket from the stack
            else:
                stack.pop()

    # If the stack is empty after iterating over the entire string, every opening bracket had a corresponding closing bracket
    # Otherwise, there were some opening brackets with no corresponding closing brackets, so return False
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
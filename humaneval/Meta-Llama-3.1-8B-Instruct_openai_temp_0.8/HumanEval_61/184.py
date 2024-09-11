```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if every opening bracket in the given string has a corresponding closing bracket.
    
    Args:
        brackets (str): A string containing only "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """

    # We use a stack to keep track of the opening brackets
    stack = []

    # We iterate over each character in the string
    for bracket in brackets:
        # If we encounter an opening bracket, we push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If we encounter a closing bracket, we check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, it means there's no corresponding opening bracket, so we return False
            if not stack:
                return False
            # If the stack is not empty, we pop the opening bracket from the stack
            else:
                stack.pop()

    # After iterating over the entire string, we check if the stack is empty
    # If the stack is empty, it means every opening bracket had a corresponding closing bracket, so we return True
    # If the stack is not empty, it means there were some opening brackets without corresponding closing brackets, so we return False
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The function uses a stack to keep track of the opening brackets and returns `False` as soon as it encounters a closing bracket without a corresponding opening bracket. Finally, the script includes several test cases to demonstrate the function's behavior.
```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
        brackets (str): A string containing only "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
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
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(("))  # False
```

This script defines a function `correct_bracketing` that takes a string of brackets as input and returns a boolean indicating whether every opening bracket has a corresponding closing bracket. It uses a stack to keep track of the opening brackets. If there's a closing bracket when the stack is empty, or if there are opening brackets left on the stack after processing the entire string, the function returns `False`. Otherwise, it returns `True`.
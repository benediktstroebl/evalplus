```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to store the opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, it means there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, if the stack is empty, it means every opening bracket has a corresponding closing bracket, so return True
    # If the stack is not empty, it means there are opening brackets with no corresponding closing brackets, so return False
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
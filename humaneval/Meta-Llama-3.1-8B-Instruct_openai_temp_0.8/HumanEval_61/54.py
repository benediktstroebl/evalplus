```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if every opening bracket in the given string has a corresponding closing bracket.
    
    Args:
        brackets (str): A string containing only '(' and ')'.
    
    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize an empty stack
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ")" and stack:
            stack.pop()
        # If the character is a closing bracket and the stack is empty, return False because there's no matching opening bracket
        elif bracket == ")" and not stack:
            return False
    
    # If the stack is empty after iterating over the entire string, return True because every opening bracket had a corresponding closing bracket
    # If the stack is not empty, return False because there are unmatched opening brackets
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()}")) #  False - added an extra closing bracket to check other cases
print(correct_bracketing(")(("))  # False
```
This script defines a function `correct_bracketing` that takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The function uses a stack to keep track of the opening brackets it encounters. If it encounters a closing bracket that doesn't match the top of the stack, it returns `False`. If it finishes iterating over the string and the stack is empty, it returns `True`. Otherwise, it returns `False` because there are unmatched opening brackets.
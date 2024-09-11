```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a counter to keep track of the opening brackets
    opening_brackets = 0
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "(":
            opening_brackets += 1
        # If the character is a closing bracket and there are no more opening brackets, return False
        elif bracket == ")" and opening_brackets == 0:
            return False
        # If the character is a closing bracket, decrement the counter
        elif bracket == ")":
            opening_brackets -= 1
    
    # If the counter is not zero, it means there are unbalanced opening brackets, so return False
    # Otherwise, return True
    return opening_brackets == 0

# Test cases
print(correct_bracketing("("))  # Output: False
print(correct_bracketing("()"))  # Output: True
print(correct_bracketing("(()())"))  # Output: True
print(correct_bracketing(")(()"))  # Output: False
```

This script defines a function `correct_bracketing` that takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. It uses a counter to keep track of the opening brackets and checks for unbalanced brackets. The test cases are included at the end to demonstrate the function's behavior.
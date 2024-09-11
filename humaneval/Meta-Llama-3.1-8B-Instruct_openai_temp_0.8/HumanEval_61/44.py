```python
def correct_bracketing(brackets: str):
    """
    Checks if a string of brackets has correct matching.

    Args:
    brackets (str): A string containing only '(' and ')'.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a counter to keep track of opening brackets
    opening_brackets = 0
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == '(':
            opening_brackets += 1
        # If the character is a closing bracket, decrement the counter
        elif bracket == ')':
            # If the counter is 0, there's no corresponding opening bracket, so return False
            if opening_brackets == 0:
                return False
            # Otherwise, decrement the counter
            opening_brackets -= 1
    
    # If the counter is not 0 after iterating over the entire string, there are unmatched opening brackets
    # Return False if the counter is not 0, True otherwise
    return opening_brackets == 0

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script implements a simple function that uses a counter to keep track of opening brackets. It iterates over the string, incrementing the counter for opening brackets and decrementing it for closing brackets. If the counter ever reaches 0 when a closing bracket is encountered, the function immediately returns False. After iterating over the entire string, the function returns True if the counter is 0 (indicating all brackets were matched) and False otherwise.
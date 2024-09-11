```python
def correct_bracketing(brackets: str):
    """
    checks if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): a string of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a counter for opening brackets
    opening_bracket_count = 0
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "(":
            opening_bracket_count += 1
        # If the character is a closing bracket, decrement the counter
        elif bracket == ")":
            opening_bracket_count -= 1
            # If the counter is negative, return False (because there's a closing bracket without an opening bracket)
            if opening_bracket_count < 0:
                return False
    
    # After iterating over the entire string, if the counter is not zero, return False (because there are unmatched brackets)
    return opening_bracket_count == 0

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
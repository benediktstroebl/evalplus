```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">"

    Returns:
        bool: Whether every opening bracket has a corresponding closing bracket
    """
    # Initialize a counter for opening brackets
    opening_brackets = 0
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "<":
            opening_brackets += 1
        # If the character is a closing bracket, decrement the counter
        elif bracket == ">":
            # If there are no opening brackets left, return False
            if opening_brackets == 0:
                return False
            opening_brackets -= 1
    
    # If the counter is not zero, there are unmatched opening brackets
    return opening_brackets == 0

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input. It uses a counter to keep track of the number of opening brackets seen so far. If it encounters a closing bracket when the counter is zero, it immediately returns `False`. After counting all the brackets, it returns `True` if the counter is zero (meaning every opening bracket had a corresponding closing bracket) and `False` otherwise.
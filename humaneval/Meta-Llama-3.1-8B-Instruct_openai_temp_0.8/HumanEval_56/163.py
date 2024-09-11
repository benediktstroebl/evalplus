```python
def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">"

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise
    """
    # Initialize a counter for opening brackets
    openings = 0
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "<":
            openings += 1
        # If the character is a closing bracket, decrement the counter
        elif bracket == ">":
            openings -= 1
            # If the counter is negative, there's an extra closing bracket, so return False
            if openings < 0:
                return False
    
    # If the counter is not zero after iterating over the entire string, there are unmatched brackets, so return False
    return openings == 0

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in the input string has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a counter to keep track of the opening brackets
    opening_brackets = 0
    
    # Iterate over each character in the input string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "<":
            opening_brackets += 1
        # If the character is a closing bracket and there are no opening brackets left, return False
        elif bracket == ">" and opening_brackets == 0:
            return False
        # If the character is a closing bracket, decrement the counter
        elif bracket == ">":
            opening_brackets -= 1
    
    # If there are any remaining opening brackets, return False
    if opening_brackets!= 0:
        return False
    
    # If the function hasn't returned False by now, every opening bracket has a corresponding closing bracket
    return True

# Test cases
if correct_bracketing("<"):
    print("Test case 1 failed")
else:
    print("Test case 1 passed")

if correct_bracketing("<>"):
    print("Test case 2 failed")
else:
    print("Test case 2 passed")

if correct_bracketing("<<><>>"):
    print("Test case 3 failed")
else:
    print("Test case 3 passed")

if correct_bracketing("><<>"):
    print("Test case 4 failed")
else:
    print("Test case 4 passed")
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. It uses a counter to keep track of the opening brackets and iterates over the input string to check for correct bracketing. The test cases are included at the end of the script to verify that the function works correctly.
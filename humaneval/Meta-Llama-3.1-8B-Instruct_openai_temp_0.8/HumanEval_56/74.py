```python
def correct_bracketing(brackets: str):
    """
    Check if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a counter for opening and closing brackets
    opening_bracket = 0

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "<":
            opening_bracket += 1
        # If the character is a closing bracket, decrement the counter
        elif bracket == ">":
            opening_bracket -= 1
            # If the counter is negative, it means there's a closing bracket without a corresponding opening bracket
            if opening_bracket < 0:
                return False

    # If the counter is not 0, it means there are opening brackets without corresponding closing brackets
    return opening_bracket == 0


# Test cases
print(correct_bracketing("<"))      # False
print(correct_bracketing("<>"))     # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>"))   # False
```

This script defines a function `correct_bracketing` that checks if every opening bracket in the input string has a corresponding closing bracket. It uses a counter to keep track of the balance between opening and closing brackets. If the counter is ever negative, it means there's a closing bracket without a corresponding opening bracket, so the function returns False. If the function finishes iterating over the string and the counter is not 0, it means there are opening brackets without corresponding closing brackets, so the function returns False. Otherwise, it returns True.
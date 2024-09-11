```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a counter to keep track of opening brackets
    opening_brackets = 0

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "(":
            opening_brackets += 1
        # If the character is a closing bracket, decrement the counter
        elif bracket == ")":
            opening_brackets -= 1
            # If the counter is negative at any point, there are more closing brackets than opening ones
            if opening_brackets < 0:
                return False

    # If there are any remaining opening brackets, there are not enough closing brackets
    return opening_brackets == 0


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
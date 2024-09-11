```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "(" and ")".

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
            # If the counter is 0, it means there's no corresponding opening bracket, so return False
            if opening_brackets == 0:
                return False
            opening_brackets -= 1

    # If the counter is not 0 after iterating over the entire string, it means there are unmatched opening brackets, so return False
    if opening_brackets!= 0:
        return False

    # If the function hasn't returned False by now, it means every opening bracket has a corresponding closing bracket, so return True
    return True

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
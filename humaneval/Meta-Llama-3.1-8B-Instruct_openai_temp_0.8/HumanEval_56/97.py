```python
def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket in the given string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """

    # Initialize a counter to keep track of the balance between opening and closing brackets
    balance = 0

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the balance
        if bracket == "<":
            balance += 1
        # If the character is a closing bracket, decrement the balance
        elif bracket == ">":
            balance -= 1
            # If the balance is negative at this point, it means there's a closing bracket without an opening one
            if balance < 0:
                return False

    # After iterating over the entire string, if the balance is not zero, it means there are opening brackets without closing ones
    return balance == 0

# Example usage:
print(correct_bracketing("<"))  # Output: False
print(correct_bracketing("<>"))  # Output: True
print(correct_bracketing("<<><>>"))  # Output: True
print(correct_bracketing("><<>"))  # Output: False
```
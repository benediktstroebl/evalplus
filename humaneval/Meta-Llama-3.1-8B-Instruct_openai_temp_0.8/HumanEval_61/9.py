```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """

    # Initialize a counter to keep track of the balance between opening and closing brackets
    balance = 0

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the balance
        if bracket == "(":
            balance += 1
        # If the character is a closing bracket, decrement the balance
        elif bracket == ")":
            balance -= 1
            # If the balance becomes negative, it means we have found a closing bracket without a corresponding opening bracket, so return False
            if balance < 0:
                return False

    # If we have iterated over the entire string and the balance is still zero, it means every opening bracket has a corresponding closing bracket, so return True
    # However, if the balance is not zero, it means we have an opening bracket without a corresponding closing bracket, so return False
    return balance == 0

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
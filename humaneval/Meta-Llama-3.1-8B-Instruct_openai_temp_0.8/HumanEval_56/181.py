```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

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

        # If the balance is negative, it means there's a closing bracket without a corresponding opening bracket
        if balance < 0:
            return False

    # If the balance is not zero at the end, it means there are opening brackets without corresponding closing brackets
    return balance == 0

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input and returns a boolean indicating whether every opening bracket has a corresponding closing bracket. The function uses a balance counter to keep track of the balance between opening and closing brackets as it iterates over the string. If it encounters a closing bracket without a corresponding opening bracket, it immediately returns False. At the end of the iteration, if the balance is not zero, it also returns False. Otherwise, it returns True.
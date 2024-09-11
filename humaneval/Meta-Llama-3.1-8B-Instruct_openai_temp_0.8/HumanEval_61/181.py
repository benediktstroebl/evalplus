```markdown
### Correct Bracketing Function

This script defines a Python function `correct_bracketing` that checks if every opening bracket in a string has a corresponding closing bracket.

#### Code

```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

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
            # If the balance is already zero, it means there's no corresponding opening bracket, so return False
            if balance == 0:
                return False
            balance -= 1
    
    # If the balance is zero at the end, it means every opening bracket has a corresponding closing bracket, so return True
    # If the balance is not zero, it means there are some opening brackets with no corresponding closing brackets, so return False
    return balance == 0

#### Example Usage

print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This code uses a counter to keep track of the balance between opening and closing brackets. It iterates over each character in the string, incrementing the counter for each opening bracket and decrementing it for each closing bracket. If a closing bracket is encountered when the counter is already zero, it means there's no corresponding opening bracket, so the function returns False. At the end, if the counter is zero, it means every opening bracket has a corresponding closing bracket, so the function returns True. Otherwise, it returns False.
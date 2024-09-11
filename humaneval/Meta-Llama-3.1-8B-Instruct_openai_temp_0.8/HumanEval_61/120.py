```python
def correct_bracketing(brackets: str):
    """
    This function checks if every opening bracket in the given string has a corresponding closing bracket.

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
        # If the balance becomes negative at any point, it means we've seen more closing brackets than opening ones
        if balance < 0:
            return False
    
    # After iterating over the entire string, if the balance is not zero, it means we have opening brackets without corresponding closing ones
    return balance == 0

# Test cases
if correct_bracketing("("):
    print("Test case 1 passed")
else:
    print("Test case 1 failed")
if correct_bracketing("()"):
    print("Test case 2 passed")
else:
    print("Test case 2 failed")
if correct_bracketing("(()())"):
    print("Test case 3 passed")
else:
    print("Test case 3 failed")
if not correct_bracketing(")(()"):
    print("Test case 4 passed")
else:
    print("Test case 4 failed")
```

This script defines a function `correct_bracketing` that takes a string of "(" and ")" as input and returns a boolean value indicating whether every opening bracket has a corresponding closing bracket. The function uses a counter to keep track of the balance between opening and closing brackets. If the balance becomes negative at any point or if the balance is not zero after iterating over the entire string, the function returns False, indicating that the string does not have correct bracketing. Otherwise, it returns True. The script also includes test cases to verify the correctness of the function.
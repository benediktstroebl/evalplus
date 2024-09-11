```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, return False because there's no corresponding opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, return True if the stack is empty (meaning every opening bracket had a corresponding closing bracket)
    # and False if the stack is not empty (meaning there were opening brackets without corresponding closing brackets)
    return not stack

# Test cases
if correct_bracketing("("):
    print("Test 1 passed")
else:
    print("Test 1 failed")

if correct_bracketing("()"):
    print("Test 2 passed")
else:
    print("Test 2 failed")

if correct_bracketing("(()())"):
    print("Test 3 passed")
else:
    print("Test 3 failed")

if not correct_bracketing(")(()"):
    print("Test 4 passed")
else:
    print("Test 4 failed")
```

This script uses a stack data structure to keep track of the opening brackets. It iterates over each character in the string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it returns False because there's no corresponding opening bracket. After iterating over the entire string, it returns True if the stack is empty (meaning every opening bracket had a corresponding closing bracket) and False if the stack is not empty (meaning there were opening brackets without corresponding closing brackets).
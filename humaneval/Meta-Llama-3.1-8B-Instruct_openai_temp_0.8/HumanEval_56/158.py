```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: Whether every opening bracket has a corresponding closing bracket.
    """
    stack = []  # Initialize an empty stack

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, return False because there's no corresponding opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # After iterating over the entire string, return True if the stack is empty and False otherwise
    return not stack


# Test cases
if correct_bracketing("<"):
    print("Test case 1 passed")
else:
    print("Test case 1 failed")

if correct_bracketing("<>"):
    print("Test case 2 passed")
else:
    print("Test case 2 failed")

if correct_bracketing("<<><>>"):
    print("Test case 3 passed")
else:
    print("Test case 3 failed")

if correct_bracketing("><<>"):
    print("Test case 4 passed")
else:
    print("Test case 4 failed")
```

This script uses a stack data structure to keep track of the opening brackets. It iterates over the string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it returns False because there's no corresponding opening bracket. After iterating over the entire string, it returns True if the stack is empty (meaning every opening bracket had a corresponding closing bracket) and False otherwise.
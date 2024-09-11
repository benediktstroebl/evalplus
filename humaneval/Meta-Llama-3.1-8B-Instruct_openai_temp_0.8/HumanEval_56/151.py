```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
        brackets (str): A string containing only "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    
    # Initialize a stack to store opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ">" and stack:
            stack.pop()
    
    # If the stack is empty after iterating over the entire string, it means every opening bracket had a corresponding closing bracket
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

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input and returns a boolean indicating whether every opening bracket has a corresponding closing bracket. The function uses a stack to keep track of the opening brackets and checks if the stack is empty at the end. The test cases at the end of the script verify the function's correctness.
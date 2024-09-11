```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack
    for bracket in brackets:  # Iterate over each character in the string
        if bracket == "<":  # If we encounter an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ">":  # If we encounter a closing bracket
            if not stack:  # If the stack is empty (no corresponding opening bracket)
                return False  # Return False
            stack.pop()  # Pop the corresponding opening bracket from the stack
    return not stack  # After iterating over the entire string, return True if the stack is empty (all brackets were properly closed), False otherwise

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that uses a stack data structure to keep track of the opening brackets encountered so far. When a closing bracket is encountered, it checks if the stack is empty, which would mean there's no corresponding opening bracket. If the stack is not empty, it pops the opening bracket from the stack. After iterating over the entire string, it returns True if the stack is empty (all brackets were properly closed) and False otherwise. The test cases are included at the end to demonstrate the function's correctness.
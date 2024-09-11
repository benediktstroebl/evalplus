```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to keep track of opening brackets

    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket, check if the stack is empty
        # If the stack is empty, there's no corresponding opening bracket for this closing bracket
        elif bracket == ")":
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # After iterating through all brackets, if the stack is empty, every opening bracket has a corresponding closing bracket
    # Otherwise, there are unpaired opening brackets
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack to keep track of the opening brackets encountered so far. It iterates through the string of brackets, pushing opening brackets onto the stack and popping them off when a corresponding closing bracket is encountered. If the stack is empty at the end of the iteration, every opening bracket has a corresponding closing bracket, and the function returns True. Otherwise, it returns False.
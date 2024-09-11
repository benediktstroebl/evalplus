```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of "<" and ">" brackets are correctly bracketed.

    Args:
        brackets (str): A string of "<" and ">" brackets.

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack
    for bracket in brackets:
        if bracket == '<':  # If we encounter an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == '>':  # If we encounter a closing bracket
            if not stack:  # If the stack is empty
                return False  # There's no corresponding opening bracket
            stack.pop()  # If the stack is not empty, pop the opening bracket
    return not stack  # If there are no opening brackets left in the stack, the string is correctly bracketed

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack data structure to keep track of the opening brackets encountered so far. When a closing bracket is encountered, it checks if the stack is empty. If it is, that means there's no corresponding opening bracket, so it returns False. If the stack is not empty, it pops the opening bracket from the stack. Finally, it checks if there are any opening brackets left in the stack. If there aren't, that means every opening bracket has a corresponding closing bracket, so it returns True.
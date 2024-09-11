```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
        brackets: A string containing "<" and ">".

    Returns:
        True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:  # Iterate over each character in the string
        if bracket == "<":  # If the character is an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ">":  # If the character is a closing bracket
            if not stack:  # If the stack is empty
                return False  # Return False because there's no corresponding opening bracket
            stack.pop()  # Otherwise, pop the corresponding opening bracket from the stack

    return not stack  # If the stack is empty after iterating over the string, return True; otherwise, return False


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

In this script, we use a stack to keep track of the opening brackets. When we encounter a closing bracket, we check if the stack is empty. If it is, that means there's no corresponding opening bracket, so we return False. Otherwise, we pop the corresponding opening bracket from the stack. After iterating over the entire string, we return True if the stack is empty (meaning every opening bracket has a corresponding closing bracket), and False otherwise.
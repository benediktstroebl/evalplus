```python
def correct_bracketing(brackets: str):
    """
    Checks if a string of brackets has every opening bracket corresponding to a closing bracket.

    Args:
    brackets (str): A string containing only "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            # Push the opening bracket onto the stack
            stack.append(bracket)
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket
            if not stack:
                return False
            # Pop the opening bracket from the stack
            stack.pop()
    # If the stack is empty, every opening bracket had a corresponding closing bracket
    return not stack


# Example usage:
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(("))  # False
print(correct_bracketing(")()("))  # False
```

This script uses a stack data structure to keep track of the opening brackets. When it encounters an opening bracket, it pushes it onto the stack. When it encounters a closing bracket, it checks if the stack is not empty (i.e., there's a corresponding opening bracket). If the stack is empty, it means there's no corresponding opening bracket, so it returns False. After processing all the brackets, it checks if the stack is empty. If it is, every opening bracket had a corresponding closing bracket, so it returns True. If the stack is not empty, there are unmatched opening brackets, so it returns False.
```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
    brackets (str): A string containing only '(' and ')'.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to keep track of opening brackets

    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == '(':
            stack.append(bracket)
        # If the bracket is a closing bracket, check if the stack is empty
        elif bracket == ')':
            # If the stack is empty, it means there's no corresponding opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # After iterating through all brackets, check if the stack is empty
    # If the stack is empty, it means every opening bracket has a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. When it encounters an opening bracket, it pushes it onto the stack. When it encounters a closing bracket, it pops the opening bracket from the stack. If the stack is empty when it encounters a closing bracket, it means there's no corresponding opening bracket, so it returns False. If the stack is not empty, it simply pops the opening bracket from the stack. After iterating through all brackets, it checks if the stack is empty. If the stack is empty, it means every opening bracket has a corresponding closing bracket, so it returns True. If the stack is not empty, it means there are some opening brackets without corresponding closing brackets, so it returns False.
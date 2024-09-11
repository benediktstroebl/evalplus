```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in a given string has a corresponding closing bracket.

    Args:
    brackets (str): A string containing only '(' and ')'.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == '(':
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ')' and stack:
            stack.pop()
    # If the stack is empty after checking all brackets, every opening bracket had a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

In this script, the `correct_bracketing` function uses a stack to keep track of the opening brackets encountered so far. For each bracket, it checks if the bracket is an opening bracket or a closing bracket. If it is an opening bracket, it pushes it onto the stack. If it is a closing bracket and the stack is not empty, it pops the opening bracket from the stack. After checking all brackets, it returns True if the stack is empty (meaning every opening bracket had a corresponding closing bracket) and False otherwise.
```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:
        if bracket == "(":  # If the bracket is an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ")":  # If the bracket is a closing bracket
            if not stack:  # If the stack is empty
                return False  # Return False because there's no corresponding opening bracket
            stack.pop()  # Pop the opening bracket from the stack

    return not stack  # Return True if the stack is empty (all brackets were matched), False otherwise


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that uses a stack to keep track of the opening brackets encountered in the string. When it encounters a closing bracket, it checks if the stack is empty. If it is, that means there's no corresponding opening bracket, so it returns False. Otherwise, it pops the opening bracket from the stack. At the end, it returns True if the stack is empty (all brackets were matched), and False otherwise.
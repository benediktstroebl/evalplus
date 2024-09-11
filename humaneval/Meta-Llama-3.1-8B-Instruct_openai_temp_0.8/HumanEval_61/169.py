```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to keep track of opening brackets

    # Iterate over each character in the string
    for bracket in brackets:
        if bracket == "(":  # If the character is an opening bracket, push it onto the stack
            stack.append(bracket)
        elif bracket == ")":  # If the character is a closing bracket
            if not stack:  # If the stack is empty, there's no corresponding opening bracket
                return False
            stack.pop()  # If the stack is not empty, pop the corresponding opening bracket

    # If the stack is empty after iterating over the string, every opening bracket had a corresponding closing bracket
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```